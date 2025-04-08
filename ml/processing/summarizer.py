from typing import List
import openai
from app.core.config import settings

class NewsSummarizer:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def summarize_articles(self, articles: List[dict]) -> str:
        """Generate a summary of multiple news articles"""
        # Combine article contents
        combined_content = "\n\n".join([
            f"Title: {article['title']}\nContent: {article['content']}"
            for article in articles
        ])

        # Generate summary using OpenAI
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a news summarizer. Create a concise, informative summary of the following news articles."},
                {"role": "user", "content": f"Please summarize these news articles:\n\n{combined_content}"}
            ],
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    async def analyze_sentiment(self, text: str) -> str:
        """Analyze the sentiment of a news article"""
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a sentiment analyzer. Analyze the sentiment of the following text and return one of: positive, negative, or neutral."},
                {"role": "user", "content": f"Analyze the sentiment of this text:\n\n{text}"}
            ],
            max_tokens=10,
            temperature=0.3
        )

        return response.choices[0].message.content.strip().lower() 