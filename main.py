from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI()

ACTIONS = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
]

# Load the SavedModel
model = tf.keras.models.load_model("keras_load_model")


# This function returns the model's predicted fluctuations for inputs rating of team A, B, difference and
# which team won.
def predict(rating_a, rating_b, rating_diff, team_A_wins):
    rating_a = rating_a/800
    rating_b = rating_b/800
    rating_diff = rating_diff/800
    state = [rating_a, rating_b, rating_diff, team_A_wins]
    q_values = model.predict(np.array([state]))
    action = np.argmax(q_values)
    fluctuation = ((rating_diff * 800) / ACTIONS[action]) + 20
    return fluctuation


class InputData(BaseModel):
    teamA: float
    teamB: float
    rankingdiff: float
    team_A_wins: int


@app.post('/')
async def prediction(data: InputData):

    rating_a = data.teamA
    rating_b = data.teamB
    if rating_a > rating_b:
        rating_diff = rating_a - rating_b
    else:
        rating_diff = rating_b - rating_a

    fluctuation = predict(rating_a, rating_b, rating_diff, data.team_A_wins)

    return {
        "prediction": fluctuation
    }
