import requests
from typing import List, Dict, Any
from .base_client import NewsClient
from app.core.config import settings

class GoogleNewsClient(NewsClient):
    """Client for fetching news from Google News API"""
    
    def __init__(self):
        self.api_key = settings.GOOGLE_NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2"
    
    async def fetch_news(self, topic: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Fetch news from Google News API"""
        url = f"{self.base_url}/everything"
        params = {
            "q": topic,
            "apiKey": self.api_key,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": max_results
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [self._format_article(article) for article in articles]
        return []
    
    async def get_source_name(self) -> str:
        return "Google News" 