from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from tensorflow.keras.models import load_model


app = FastAPI()

# Load the trained model
model_filename = r'C:\Users\aayus\your_model.h5'

model = load_model(model_filename)



class PredictionRequest(BaseModel):
    team_1_ranking: float
    team_1_titles: float
    team_1_win_percentage_odi: float
    team_1_wc_matches: float
    team_1_wc_match_won: float
    team_1_win_percent_wc: float
    team_1_wc_match_loss: float
    team_1_loss_percent_wc: float
    team_1_recent_points: float
    team_1_rating: float

    team_2_ranking: float
    team_2_titles: float
    team_2_win_percentage_odi: float
    team_2_wc_matches: float
    team_2_wc_match_won: float
    team_2_win_percent_wc: float
    team_2_wc_match_loss: float
    team_2_loss_percent_wc: float
    team_2_recent_points: float
    team_2_rating: float


class PredictionResponse(BaseModel):
    prediction: int


@app.post("/predict")
async def predict(data: PredictionRequest):
    try:
        # Prepare the input data
        input_data = np.array([[
            data.team_1_ranking, data.team_1_titles, data.team_1_win_percentage_odi,
            data.team_1_wc_matches, data.team_1_wc_match_won, data.team_1_win_percent_wc,
            data.team_1_wc_match_loss, data.team_1_loss_percent_wc, data.team_1_recent_points,
            data.team_1_rating,
            data.team_2_ranking, data.team_2_titles, data.team_2_win_percentage_odi,
            data.team_2_wc_matches, data.team_2_wc_match_won, data.team_2_win_percent_wc,
            data.team_2_wc_match_loss, data.team_2_loss_percent_wc, data.team_2_recent_points,
            data.team_2_rating
        ]])

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Return the prediction
        return {"prediction": int(prediction)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
