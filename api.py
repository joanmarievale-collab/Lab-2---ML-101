from fastapi import FastAPI, Form
from typing import List
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from starlette.responses import FileResponse  # Import from starlette

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", response_class=FileResponse)
async def read_root():
    return "ml101.html"

@app.post("/submit_quiz", response_class=JSONResponse)
async def submit_quiz(
    q1: List[str] = Form([]),
    q2: List[str] = Form([]),
    q3: List[str] = Form([]),
    q4: List[str] = Form([]),
    q5: List[str] = Form([]),
):
    correct_answers = {
        "q1": ["Supervised Learning", "Unsupervised Learning", "Semi-Supervised Learning", "Reinforcement Learning"],
        "q2": ["Data Collection", "Data Preprocessing", "Model Selection", "Model Training"],
        "q3": ["Linear Regression", "Decision Trees", "Random Forest", "Naive Bayes"],
        "q4": ["Spam Detection", "Image Recognition", "Stock Market Prediction", "Weather Forecasting"],
        "q5": ["Overfitting", "Underfitting", "Data Quality", "Model Explainability"],
    }

    all_correct = True
    for key, correct in correct_answers.items():
        selected = eval(key) # Dynamically gets the list from the Form data
        if not (len(selected) == len(correct) and all(item in correct for item in selected)):
            all_correct = False
            break

    if all_correct:
        return JSONResponse({"result": "All answers are correct! 🎉"})
    else:
        return JSONResponse({"result": "Some answers are incorrect. Try again! ❌"})
    
@app.get("/favicon.ico", response_class=FileResponse)
async def favicon():
    if os.path.exists("favicon.ico"):
        return "favicon.ico"
    else:
        return None