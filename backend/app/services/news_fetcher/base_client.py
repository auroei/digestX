from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime

class NewsClient(ABC):
    """Abstract base class for news API clients"""
    
    @abstractmethod
    async def fetch_news(self, topic: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Fetch news articles for a given topic"""
        pass
    
    @abstractmethod
    async def get_source_name(self) -> str:
        """Get the name of the news source"""
        pass
    
    def _format_article(self, raw_article: Dict[str, Any]) -> Dict[str, Any]:
        """Format a raw article into a standardized format"""
        return {
            "title": raw_article.get("title", ""),
            "content": raw_article.get("content", ""),
            "url": raw_article.get("url", ""),
            "source": self.get_source_name(),
            "published_at": raw_article.get("publishedAt", datetime.utcnow().isoformat()),
            "author": raw_article.get("author", ""),
            "image_url": raw_article.get("urlToImage", "")
        } 