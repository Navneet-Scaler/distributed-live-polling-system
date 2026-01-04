from typing import Dict
from app.core.redis_manager import RedisManager


class PollingService:
    def __init__(self):
        self.redis = RedisManager()

    async def vote(self, poll_id: str, option_id: str) -> None:
        key = f"poll:{poll_id}"
        await self.redis.increment(key, option_id)

    async def get_results(self, poll_id: str) -> Dict[str, int]:
        key = f"poll:{poll_id}"
        return await self.redis.get_all(key)
