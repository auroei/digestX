# DigestX Architecture

## System Overview

DigestX is a distributed system composed of several components working together to provide news aggregation and summarization services. The system follows a microservices architecture pattern with clear separation of concerns.

## Components

### 1. Backend API Service
- Built with FastAPI
- Handles HTTP requests from the frontend
- Manages user topics and preferences
- Provides endpoints for news retrieval and summarization
- Uses PostgreSQL for persistent storage
- Implements Redis for caching

### 2. Worker Service
- Runs background tasks
- Fetches news from multiple sources
- Generates summaries using LLMs
- Cleans up old data
- Runs on a schedule (every 6 hours for news fetching, daily for cleanup)

### 3. Database (PostgreSQL)
- Stores user data
- Stores news articles
- Stores topic preferences
- Stores generated summaries

### 4. Cache (Redis)
- Caches API responses
- Stores temporary data
- Manages rate limiting

## Data Flow

1. **News Collection**:
   - Worker service periodically fetches news from configured sources
   - News is stored in the database
   - Duplicate articles are filtered out

2. **Summarization**:
   - Worker service processes new articles
   - Uses OpenAI's GPT-4 for summarization
   - Stores summaries in the database

3. **User Interaction**:
   - Users access the frontend
   - Frontend makes API calls to the backend
   - Backend retrieves data from database/cache
   - Results are returned to the user

## Security

- API keys are stored as environment variables
- JWT authentication for user access
- Rate limiting on API endpoints
- Input validation and sanitization
- CORS configuration for frontend access

## Scalability

- Containerized services for easy scaling
- Stateless API design
- Caching layer for performance
- Background processing for heavy tasks
- Database indexing for efficient queries

## Monitoring and Logging

- Structured logging in all services
- Error tracking and reporting
- Performance monitoring
- Health checks for services

## Deployment

- Docker-based deployment
- Docker Compose for local development
- CI/CD pipeline for automated testing and deployment
- Environment-specific configurations 