from pydantic import BaseModel
from typing import List

class QuizSubmission(BaseModel):
    q1: List[str] = []
    q2: List[str] = []
    q3: List[str] = []
    q4: List[str] = []
    q5: List[str] = []
    q6: List[str] = []
    q7: List[str] = []
    q8: List[str] = []
    q9: List[str] = []
    q10: List[str] = []
