# ✦ AnikaAI — CV Builder Chatbot

A modern AI-powered desktop chatbot that reads your personal information and generates a professional CV — built with Python, Tkinter, and Ollama.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🤖 **AI-powered CV generation** using local Ollama models
- 📄 **Upload your info** as a TXT file — auto-loaded on startup
- 📥 **Export CV as PDF** with professional formatting
- 💬 **ChatGPT-style UI** with sidebar and multiple chat sessions
- 💾 **Persistent chat history** — saved across sessions
- 🔄 **Switch AI models** from dropdown (llama, mistral, gemma, phi)
- 🔒 **100% local & private** — no data sent to the internet

---

## 🖥️ Screenshots

<img width="976" height="632" alt="image" src="https://github.com/user-attachments/assets/72265f5a-a3a7-48de-beda-10b5ee250734" />


## 🚀 Getting Started

### 1. Install Ollama
Download from [https://ollama.com](https://ollama.com) and install it.

Then pull a model:
```bash
ollama pull mistral
```

### 2. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/AnikaAI-CV-Builder.git
cd AnikaAI-CV-Builder
```

### 3. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install ollama fpdf2
```

### 5. Add your info file
Create a `info.txt` file inside the `backend/` folder with your personal details:
```
Name: Your Name
Email: your@email.com
Phone: 01700000000
...
```

### 6. Run the app
```bash
cd backend
python main.py
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core language |
| Tkinter | Desktop UI |
| Ollama | Local AI engine |
| fpdf2 | PDF export |

---

## 💡 How to Use

1. Run `python main.py` — Ollama starts automatically
2. Your `info.txt` file loads automatically (shown in sidebar)
3. Type **"Create my CV"** in the chat
4. Click **📥 Export CV as PDF** to save

---

## 📁 Project Structure

```
AnikaAI-CV-Builder/
├── backend/
│   ├── main.py          # Main application
│   ├── info.txt         # Your personal info (not pushed to git)
│   └── chat_history.json# Auto-generated chat history
├── .gitignore
└── README.md
```

---

## 👩‍💻 Built By

**Asma Anika Shahabuddin** — Full Stack Developer & CS Student from Dhaka, Bangladesh.

- 🌐 Fiverr: [CodeWithAnika](https://fiverr.com)
- 💼 Upwork: [CodeWithAnika](https://upwork.com)
- 🐙 GitHub: [github.com/anika92](https://github.com/anika92)

---

## 📄 License

MIT License — feel free to use and modify!
