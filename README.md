AI Note-Taker

An AI-powered note-taking and productivity assistant that helps users organize thoughts, summarize long text, generate task lists, and store structured notes. Built with FastAPI, React, SQLAlchemy, and JWT authentication, this project is designed to feel like a personal case-manager assistant that helps users stay organized and productive.

✨ Features
AI-Powered Tools

Summarize long text into clear action steps

Generate tasks, bullet points, or structured notes

Rewrite, organize, or expand rough ideas

Create follow-up prompts based on user context

Core Application Features

Secure user authentication (JWT)

CRUD endpoints for:

Notes

Tasks

Categories

Persistent relational database (PostgreSQL or SQLite depending on environment)

Modern, responsive React UI

Full API documentation via OpenAPI / Swagger

Fully containerized with Docker

🧠 Tech Stack
Backend

FastAPI

SQLAlchemy ORM

PostgreSQL / SQLite

JWT Authentication

Pydantic Models

Docker / Docker Compose

Pytest (unit tests)

Frontend

React (Vite or CRA)

Tailwind CSS

Axios for API requests

AI Integration

OpenAI API (GPT-4.1 / GPT-o series)

📂 Project Structure
ai-note-taker/
│── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routers/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database.py
│   │   ├── auth/
│   │   └── services/ai_service.py
│   ├── tests/
│   └── requirements.txt
│
│── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
│── docker-compose.yml
│── README.md

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/<your-username>/ai-note-taker.git
cd ai-note-taker

Backend Setup (FastAPI)
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r backend/requirements.txt

4. Run the FastAPI server
uvicorn app.main:app --reload


Backend will run at:
http://localhost:8000

Swagger docs:
http://localhost:8000/docs

Frontend Setup (React)
1. Install packages
cd frontend
npm install

2. Start development server
npm run dev


Frontend will run at:
http://localhost:5173

🐳 Docker Setup (Full App)
docker-compose up --build


This launches:

FastAPI server

React client

Database

🧪 Running Tests
pytest -q

🔑 Environment Variables

Create a .env file inside backend/:

DATABASE_URL=postgresql://user:password@db:5432/notes
JWT_SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_api_key

📘 API Examples
Create a Note
POST /notes/
{
  "title": "Lecture Notes",
  "content": "Today we covered FastAPI routing."
}

AI Summarization
POST /ai/summarize
{
  "text": "long text here..."
}

Response
{
  "summary": "Here are the main takeaways..."
}

📈 Future Roadmap

Voice-to-text transcription

Daily/weekly AI summaries

Calendar integration

Smart tagging + topic clustering

Task auto-prioritization

Mobile version

🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to add.