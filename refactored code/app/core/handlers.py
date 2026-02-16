correct_answers = {
    "q1": ["Supervised Learning", "Unsupervised Learning", "Semi-Supervised Learning", "Reinforcement Learning"],
    "q2": ["Data Collection", "Data Preprocessing", "Model Selection", "Model Training"],
    "q3": ["Linear Regression", "Decision Trees", "Random Forest", "Naive Bayes"],
    "q4": ["Spam Detection", "Image Recognition", "Stock Market Prediction", "Weather Forecasting"],
    "q5": ["Overfitting", "Underfitting", "Data Quality", "Model Explainability"],
    "q6": ["Removing duplicate values", "Handling missing values", "Identifying and removing outliers"],
    "q7": ["It ensures all features have the same scale, preventing dominance of large-valued features.", 
           "It improves the performance of gradient-based optimization algorithms.", 
           " It is useful for distance-based algorithms like KNN and SVM."],
    "q8": ["NumPy", "Pandas", "Scikit-learn"],
    "q9": ["Data collection", "Data cleaning and preprocessing", "Model training and evaluation", "Deploying the trained model"],
    "q10": ["Removing rows with missing values", "Replacing missing values with the mean, median, or mode", 
            "Using advanced techniques like KNN imputation"],
}

def validate_quiz_answers(form_data: dict) -> str:
    for key, correct in correct_answers.items():
        selected = form_data.get(key, [])
        if not (len(selected) == len(correct) and all(item in correct for item in selected)):
            return "Some answers are incorrect. Try again! ❌"
    return "All answers are correct! 🎉"
