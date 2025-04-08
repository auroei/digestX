from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    source = Column(String)
    url = Column(String, unique=True)
    published_at = Column(DateTime, default=datetime.utcnow)
    topic = Column(String, index=True)
    summary = Column(Text, nullable=True)
    sentiment = Column(String, nullable=True)
    
    # Relationships
    user_topics = relationship("UserTopic", back_populates="articles")

class UserTopic(Base):
    __tablename__ = "user_topics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    articles = relationship("NewsArticle", back_populates="user_topics")
    user = relationship("User", back_populates="topics") 