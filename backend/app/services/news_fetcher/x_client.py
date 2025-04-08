import requests
from typing import List, Dict, Any
from .base_client import NewsClient
from app.core.config import settings

class XNewsClient(NewsClient):
    """Client for fetching news from X API"""
    
    def __init__(self):
        self.api_key = settings.X_API_KEY
        self.base_url = "https://api.twitter.com/2"  # Update with actual X API endpoint
    
    async def fetch_news(self, topic: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Fetch news from X API"""
        # This is a placeholder implementation
        # Update with actual X API implementation when available
        url = f"{self.base_url}/search/tweets"
        params = {
            "q": topic,
            "count": max_results,
            "tweet_mode": "extended"
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        try:
            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                tweets = response.json().get("statuses", [])
                return [self._format_tweet(tweet) for tweet in tweets]
        except Exception as e:
            print(f"Error fetching from X API: {str(e)}")
        return []
    
    def _format_tweet(self, tweet: Dict[str, Any]) -> Dict[str, Any]:
        """Format a tweet into a standardized article format"""
        return {
            "title": tweet.get("full_text", "")[:100] + "...",
            "content": tweet.get("full_text", ""),
            "url": f"https://twitter.com/user/status/{tweet.get('id_str', '')}",
            "source": "X",
            "published_at": tweet.get("created_at", ""),
            "author": tweet.get("user", {}).get("screen_name", ""),
            "image_url": tweet.get("entities", {}).get("media", [{}])[0].get("media_url_https", "")
        }
    
    async def get_source_name(self) -> str:
        return "X" 