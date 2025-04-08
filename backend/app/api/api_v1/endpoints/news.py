from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.services.news_service import NewsService
from app.models.news import NewsArticle
from app.api.deps import get_db

router = APIRouter()

@router.get("/topics/{topic}", response_model=List[NewsArticle])
async def get_topic_news(
    topic: str,
    days: int = 1,
    db: Session = Depends(get_db)
):
    """Get news articles for a specific topic"""
    news_service = NewsService(db)
    articles = await news_service.get_topic_news(topic, days)
    return articles

@router.post("/topics/{topic}/refresh")
async def refresh_topic_news(
    topic: str,
    db: Session = Depends(get_db)
):
    """Refresh news articles for a specific topic"""
    news_service = NewsService(db)
    try:
        articles = await news_service.process_and_store_news(topic)
        return {"message": f"Successfully processed {len(articles)} new articles"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 