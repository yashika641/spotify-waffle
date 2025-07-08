from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.models import *
# Import all route files
from backend.app.routes import (
    auth,
    user,
    song,
    album,
    artist,
    playlist,
    like,
    search_logs,
    follow,
    listening_history,
)
import logging

logging.basicConfig(level=logging.DEBUG)
app = FastAPI(
    title="Spotify Clone API",
    description="All APIs for music, user, playlist, auth, and recommendations",
    version="1.0.0",
)

# ✅ Enable CORS (if testing from frontend / Postman)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register all routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(song.router)
# app.include_router(album.router)
app.include_router(artist.router)
# app.include_router(playlist.router)
# app.include_router(like.router)
# app.include_router(search_logs.router)
# app.include_router(follow.router)
# app.include_router(listening_history.router)

# ✅ Root route (optional)
@app.get("/")
def root():
    return {"message": "Welcome to the Spotify Clone API!"}
