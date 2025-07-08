from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
import os

# Import functions from your recommendation pipeline
from models.model_codes.collaborative_filtering import preprocessing, cf, recommend
from models.utils.logger import get_logger

logger = get_logger('recommender_route')

router = APIRouter(
    prefix="/recommend",
    tags=["Recommendations"]
)

# Load and preprocess data once when the app starts
DATA_PATH = r"C:\Users\palya\Desktop\spotify clone\spotify-waffle\models\data\tracks_features.csv"

try:
    df_raw = pd.read_csv(DATA_PATH)
    df_encoded, original_df = preprocessing(df_raw)
    similarity_df = cf(df_encoded, original_df)
    logger.info("Model loaded and similarity matrix built.")
except Exception as e:
    logger.error("Error during model load: %s", str(e))
    df_encoded, original_df, similarity_df = None, None, None


# Request body model
class TrackInput(BaseModel):
    track_name: str


# Endpoint: POST /recommend/song
@router.post("/song", response_model=List[str])
def get_similar_songs(input_track: TrackInput):
    try:
        if similarity_df is None or original_df is None:
            raise HTTPException(status_code=500, detail="Model not loaded")

        recommendations = recommend(similarity_df, original_df, input_track.track_name, top_n=5)
        if isinstance(recommendations, str):  # Track not found
            raise HTTPException(status_code=404, detail=recommendations)
        return recommendations

    except Exception as e:
        logger.error("Error in recommendation endpoint: %s", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")
