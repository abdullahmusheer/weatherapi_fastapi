from fastapi import FastAPI, HTTPException
import json

from weather import get_weather
from cache import get_cache, save_cache


from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi import Request

limiter = Limiter(key_func=get_remote_address) #basically here we add limiter functionality from slowapi lib 
                                               # and it basically gets the remote address to make sure that the actor is not rogue

app = FastAPI()

app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)

@app.get("/weather/{city}")
@limiter.limit("10/minute")
def weather(request: Request, city: str):

    cached = get_cache(city)
    if cached:
        return{
            "source": "cached",
            "weather": json.loads(cached)
        }
    weather = get_weather(city)

    if weather is None:
        raise HTTPException(
            status_code=404,
            detail="city not found man"
        )
    save_cache(city, weather)

    return{
        "source":"api",
        "weather": json.loads(weather)
    }
