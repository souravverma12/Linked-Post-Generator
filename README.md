# 🧠 LinkedIn Post Generator using LLaMA 3.2 + Streamlit

A context-aware LinkedIn post generator built using **LLaMA 3.2**, **LangChain**, **GroqCloud**, and **Streamlit**. This app generates human-like LinkedIn posts based on topic, language, and length using few-shot learning from real-world post samples.

---

## 🚀 Features

- ✅ Generate contextually rich LinkedIn posts
- 📄 Filter posts by **length**, **language** (English/Hinglish), and **topic/tag**
- 🤖 Uses **Groq-hosted LLaMA 3.2** for blazing fast generation
- 🧠 Implements **prompt engineering** and **few-shot learning**
- 💡 Streamlit-powered UI for real-time post creation

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend Logic:** Python, LangChain
- **LLM API:** GroqCloud (LLaMA 3.2 70B)
- **Data:** JSON-based post dataset
- **LLM Prompting Techniques:** Few-shot prompting, zero-shot metadata extraction

---

## 📂 Project Structure

```bash
📁 data/
    ├── raw_posts.json         # Original input posts (no metadata)
    └── processed_posts.json   # Metadata-enriched posts used for few-shot examples

📄 few_shot.py                 # Loads filtered examples by tag/length/language
📄 llm_helper.py              # Connects to Groq LLaMA 3.2 via API
📄 main.py                    # Streamlit UI logic
📄 post_generator.py          # Builds prompts and generates posts
📄 preprocess.py              # Extracts metadata and standardizes tags using LLM
