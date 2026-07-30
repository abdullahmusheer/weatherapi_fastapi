import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
    
)

CACHE_TIME = 43200  #12 hours

def get_cache(city):
    return redis_client.get(city.lower())

def save_cache(city, data):
    redis_client.set(
        city.lower(),
        data,
        ex=CACHE_TIME
    )

