# 📖 The Life of Adam (Ollama + RAG)

This is a **chatbot powered by Ollama** that can answer your questions about **the life and times of Adam**.  
It uses **retrieval-augmented generation (RAG)** — meaning it pulls information from a dataset (`adam-life.txt`) and combines it with a language model response.  
The bot also **remembers your previous messages** for a continuous storytelling and Q&A experience.

---

## ✨ Features
- Loads a dataset of **biographical notes on Adam** from a text file.
- Uses **embeddings** to retrieve the most relevant passages.
- Streams responses from a **language model** in real time.
- Keeps track of **conversation history** for contextual, evolving dialogue.
- Runs in an **interactive chat loop** until you type `quit`, `exit`, or `bye`.

---

## 📂 Project Structure
├── adam-life.txt # Dataset of Adam's life events
├── main.py # Chatbot source code
└── README.md # Project documentation



---

## ⚙️ Requirements
Before running, make sure you have:

1. **Python 3.9+**  
   [Download here](https://www.python.org/downloads/)

2. **Ollama** installed and running locally  
   [Install Ollama](https://ollama.ai)

3. **Required models** pulled into Ollama:
   ```bash
   ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
   ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
