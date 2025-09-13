import ollama

# Load the dataset
dataset = []
with open("adam-smith-a-biography.txt", "r", encoding="utf-8") as file:
    dataset = file.readlines()
    print(f'Loaded {len(dataset)} entries')

# Retrieval system
EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

VECTOR_DB = []

def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))

for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    print(f'Added chunk {i+1}/{len(dataset)} to the database')

def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5
    return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

# --- Chatbot loop with memory ---
messages = []

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chat ended. Goodbye!")
        break

    # Retrieve context for *this* user query
    retrieved_knowledge = retrieve(user_input)
    context_text = "\n".join([f' - {chunk}' for chunk, _ in retrieved_knowledge])

    # Update system prompt each turn with context
    system_prompt = f"""You are a helpful chatbot.
Use only the following pieces of context to answer the user. 
If the context does not contain an answer, say you don’t know.

Context:
{context_text}
"""

    # Build message list: system prompt + full conversation history + new user msg
    convo = [{"role": "system", "content": system_prompt}] + messages + [
        {"role": "user", "content": user_input}
    ]

    # Stream bot reply
    print("Bot:", end=" ", flush=True)
    response_text = ""
    stream = ollama.chat(model=LANGUAGE_MODEL, messages=convo, stream=True)

    for chunk in stream:
        content = chunk["message"]["content"]
        print(content, end="", flush=True)
        response_text += content

    print()  # newline after bot finishes

    # Save both user & assistant messages into history
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": response_text})
