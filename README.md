# GenFlow Studio

**GenFlow Studio** is an AI-powered autonomous content generation pipeline. It simulates a multi-agent system where each agent handles a specific task — from research to writing, reviewing, and visual design — to produce publish-ready content based on a given topic.

> Built with Next.js + FastAPI + OpenAI-compatible models  
> Designed for modern content teams and AI infrastructure explorers.

---

## 🧠 Features

- 🔍 **ResearchAgent**: Automatically fetches relevant context from Wikipedia
- ✍️ **WriterAgent**: Generates a 3-paragraph introductory article using LLMs (e.g., GPT-4o via OpenRouter)
- 🧠 **ReviewerAgent**: Analyzes generated content for tone, clarity, structure, and quality
- 🎨 **DesignerAgent**: Suggests or generates visual illustrations for the topic
- ⚡ Fully automated pipeline from input to publish-ready output
- 🌐 Built with a modular, multi-agent architecture

---

## 🚀 Tech Stack

### Frontend

- [Next.js 15 (App Router)](https://nextjs.org)
- Tailwind CSS
- TypeScript

### Backend

- [FastAPI](https://fastapi.tiangolo.com)
- Python 3.13+
- OpenAI-compatible SDKs (OpenRouter.ai / Local LLMs)

---

## 📦 Project Structure

```
genflow-backend/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # API keys & env
│   └── agents/
│       ├── research_agent.py   # Wikipedia summarizer
│       ├── writer_agent.py     # LLM writer
│       ├── reviewer_agent.py   # Content critic
│       └── designer_agent.py   # Image generator
│
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/genflow-studio.git
cd genflow-studio
```

### 2. Backend Setup (FastAPI)

```bash
cd genflow-backend
python -m venv venv
source venv/bin/activate  # or venv/Scripts/activate on Windows

pip install -r requirements.txt
```

Create a `.env` file in `genflow-backend/`:

````env
# For OpenRouter (recommended)
OPENROUTER_API_KEY=your_openrouter_api_key

Run the API:

```bash
uvicorn app.main:app --reload
````

---

### 3. Frontend Setup (Next.js)

```bash
cd genflow-frontend
npm install
npm run dev
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## 📚 Example Topics to Try

- Artificial Intelligence
- Climate Change
- Cybersecurity
- Retro-Futurism
- Mars Colonization

---

## 💡 Future Enhancements

- CMS export (Ghost / Notion / Wordpress)
- Multi-style writing (technical, marketing, educational)
- User authentication + content history
- LangGraph/CrewAI orchestration logic

---

## 🌟 Acknowledgments

- [OpenRouter.ai](https://openrouter.ai)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [Unsplash](https://unsplash.com)
