from typing import List, Optional
from datetime import datetime, timedelta
import requests
from app.core.config import settings
from app.models.news import NewsArticle
from sqlalchemy.orm import Session

class NewsService:
    def __init__(self, db: Session):
        self.db = db
        self.google_news_api_key = settings.GOOGLE_NEWS_API_KEY
        self.x_api_key = settings.X_API_KEY

    async def fetch_google_news(self, topic: str, max_results: int = 10) -> List[dict]:
        """Fetch news from Google News API"""
        url = f"https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "apiKey": self.google_news_api_key,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": max_results
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        return []

    async def fetch_x_news(self, topic: str, max_results: int = 10) -> List[dict]:
        """Fetch news from X API"""
        # Implementation for X API will go here
        # This is a placeholder as X API implementation details may vary
        return []

    async def process_and_store_news(self, topic: str) -> List[NewsArticle]:
        """Process and store news articles for a given topic"""
        google_news = await self.fetch_google_news(topic)
        x_news = await self.fetch_x_news(topic)
        
        all_news = google_news + x_news
        stored_articles = []
        
        for article in all_news:
            # Check if article already exists
            existing = self.db.query(NewsArticle).filter(
                NewsArticle.url == article.get("url")
            ).first()
            
            if not existing:
                new_article = NewsArticle(
                    title=article.get("title"),
                    content=article.get("content"),
                    source=article.get("source", {}).get("name"),
                    url=article.get("url"),
                    published_at=datetime.fromisoformat(article.get("publishedAt")),
                    topic=topic
                )
                self.db.add(new_article)
                stored_articles.append(new_article)
        
        self.db.commit()
        return stored_articles

    async def get_topic_news(self, topic: str, days: int = 1) -> List[NewsArticle]:
        """Get news articles for a specific topic within the last N days"""
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        
        articles = self.db.query(NewsArticle).filter(
            NewsArticle.topic == topic,
            NewsArticle.published_at >= cutoff_date
        ).all()
        
        return articles 