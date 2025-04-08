import asyncio
import logging
from datetime import datetime, timedelta
from app.tasks import fetch_and_summarize_news, cleanup_old_articles

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_scheduled_tasks():
    """Run scheduled tasks at specified intervals"""
    while True:
        try:
            # Run news fetching and summarization every 6 hours
            await fetch_and_summarize_news()
            logger.info("Completed news fetching and summarization task")
            
            # Run cleanup every 24 hours
            if datetime.utcnow().hour == 0:  # Run at midnight UTC
                await cleanup_old_articles()
                logger.info("Completed cleanup task")
            
            # Sleep for 1 hour before next check
            await asyncio.sleep(3600)
            
        except Exception as e:
            logger.error(f"Error in scheduled tasks: {str(e)}")
            await asyncio.sleep(300)  # Sleep for 5 minutes on error

if __name__ == "__main__":
    logger.info("Starting worker service...")
    asyncio.run(run_scheduled_tasks()) 