from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    servers=[
        {
            "url": "https://gpt-stripe-store-main.vercel.app/",
            "description": "Production environment",
        }
    ]
)

@app.get("/getColorByMood/")
async def get_color_by_mood(mood: Optional[str] = None):
    mood_color_map = {
        "happy": "yellow",
        "sad": "blue",
        "angry": "red",
        "relaxed": "green",
    }
    return {"color": mood_color_map.get(mood, "white")}  # Default to "white" if mood not found
