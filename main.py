from fastapi import FastAPI
from typing import Optional
from fastapi.responses import FileResponse

app = FastAPI(
    servers=[
        {
            "url": "https://gpt-stripe-store-main.vercel.app/",
            "description": "Production environment",
        }
    ]
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the GPT Stripe Store API"}

@app.get("/getColorByMood/")
async def get_color_by_mood(mood: Optional[str] = None):
    mood_color_map = {
        "happy": "yellow",
        "sad": "blue",
        "angry": "red",
        "relaxed": "green",
    }
    return {"color": mood_color_map.get(mood, "white")}  # Default to "white" if mood not found

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")  # Replace with the path to your favicon file
