import redis
import os
from typing import Text, List


class Queue(object):

    def __init__(self) -> None:
        self.client = redis.StrictRedis(encoding="utf-8", decode_responses=True)
    
    def create_pipeline(self) -> redis.StrictRedis.pipeline:
        """Create a pipeline using for multiple commands in single request."""
        return self.client.pipeline()
    
    def count(self, key_name: Text):
        """Get item count in list"""
        return self.client.scard(key_name)
    
    def lpush(self, key_name: Text, item: str) -> Text:
        """Pushing element to the right side of the list."""
        return self.client.lpush(key_name, item)

    def rpop(self, key_name: Text) -> Text:
        """Popping element from the left side of the list."""
        return self.client.rpop(key_name)
