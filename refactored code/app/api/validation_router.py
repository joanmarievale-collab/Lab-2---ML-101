from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from typing import List
from core.handlers import validate_quiz_answers

router = APIRouter()

@router.post("/submit_quiz", response_class=JSONResponse)
async def submit_quiz(
    q1: List[str] = Form([]),
    q2: List[str] = Form([]),
    q3: List[str] = Form([]),
    q4: List[str] = Form([]),
    q5: List[str] = Form([]),
    q6: List[str] = Form([]),
    q7: List[str] = Form([]),
    q8: List[str] = Form([]),
    q9: List[str] = Form([]),
    q10: List[str] = Form([]),
):
    result = validate_quiz_answers(locals())
    return JSONResponse({"result": result})
