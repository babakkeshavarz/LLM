# 🐱 Cat Facts Chatbot (Ollama + RAG)

This is a **chatbot powered by Ollama** that can answer your questions about cats 🐾.  
It uses **retrieval-augmented generation (RAG)** — meaning it pulls facts from a dataset (`cat-facts.txt`) and combines them with a language model response.  
The bot also **remembers your previous messages** for a continuous chat experience.

---

## ✨ Features
- Loads a dataset of **cat facts** from a text file.
- Uses **embeddings** to retrieve the most relevant facts.
- Streams responses from a **language model** in real time.
- Keeps track of **conversation history** for context.
- Runs in an **interactive chat loop** until you type `quit`, `exit`, or `bye`.

---

## 📂 Project Structure


## Installation

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
