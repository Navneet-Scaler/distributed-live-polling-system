import redis.asyncio as redis
from app.core.config import settings


class RedisManager:
    def __init__(self):
        # single-node for now (we’ll shard later)
        self.client = redis.from_url(settings.redis_nodes[0], decode_responses=True)

    async def increment(self, key: str, field: str):
        await self.client.hincrby(key, field, 1)

    async def get_all(self, key: str):
        data = await self.client.hgetall(key)
        return {k: int(v) for k, v in data.items()}
