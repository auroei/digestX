# DigestX - AI-Powered News Digest

DigestX is a web application that aggregates news from multiple sources (X API, Google News API) and uses LLMs to generate personalized daily summaries on topics of your choice.

## Features

- News aggregation from multiple sources
- AI-powered summarization using LLMs
- Personalized topic selection
- Daily digest delivery
- Modern, responsive web interface

## Tech Stack

### Frontend
- Next.js 14
- React
- Tailwind CSS
- TypeScript

### Backend
- Python FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Redis (for caching)

### AI/ML
- OpenAI API
- Hugging Face Transformers

## Project Structure

```
digestX/
├── frontend/           # Next.js frontend application
├── backend/           # FastAPI backend service
├── ml/               # ML models and processing
├── docker/           # Docker configuration files
└── docs/            # Documentation
```

## Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker
- PostgreSQL
- Redis

### Development Setup

1. Clone the repository
2. Set up environment variables (see `.env.example`)
3. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd backend
   pip install -r requirements.txt
   ```
4. Start the development servers:
   ```bash
   # Frontend
   cd frontend
   npm run dev

   # Backend
   cd backend
   uvicorn main:app --reload
   ```

## Environment Variables

Create `.env` files in both frontend and backend directories based on `.env.example`:

### Frontend (.env)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/digestx
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=your_openai_key
X_API_KEY=your_x_api_key
GOOGLE_NEWS_API_KEY=your_google_news_api_key
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
