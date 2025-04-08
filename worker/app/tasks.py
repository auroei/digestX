from datetime import datetime, timedelta
from typing import List
from sqlalchemy.orm import Session
from app.services.news_fetcher.google_news_client import GoogleNewsClient
from app.services.news_fetcher.x_client import XNewsClient
from app.services.news_service import NewsService
from app.ml.processing.summarizer import NewsSummarizer
from app.db.session import SessionLocal
from app.models.news import NewsArticle, UserTopic

async def fetch_and_summarize_news():
    """Background task to fetch and summarize news for all active topics"""
    db = SessionLocal()
    try:
        # Get all active topics
        active_topics = db.query(UserTopic).filter(UserTopic.is_active == True).all()
        
        # Initialize news clients
        google_client = GoogleNewsClient()
        x_client = XNewsClient()
        news_service = NewsService(db)
        summarizer = NewsSummarizer()
        
        for topic in active_topics:
            # Fetch news from all sources
            google_news = await google_client.fetch_news(topic.topic)
            x_news = await x_client.fetch_news(topic.topic)
            
            # Process and store news
            articles = await news_service.process_and_store_news(topic.topic)
            
            # Generate summary for the day's news
            if articles:
                summary = await summarizer.summarize_articles(articles)
                
                # Update the latest summary for the topic
                topic.latest_summary = summary
                topic.last_updated = datetime.utcnow()
                db.commit()
                
    except Exception as e:
        print(f"Error in background task: {str(e)}")
    finally:
        db.close()

async def cleanup_old_articles():
    """Background task to clean up old articles"""
    db = SessionLocal()
    try:
        # Delete articles older than 30 days
        cutoff_date = datetime.utcnow() - timedelta(days=30)
        db.query(NewsArticle).filter(NewsArticle.published_at < cutoff_date).delete()
        db.commit()
    except Exception as e:
        print(f"Error cleaning up old articles: {str(e)}")
    finally:
        db.close() 