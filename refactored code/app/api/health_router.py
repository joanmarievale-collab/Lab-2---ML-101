from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", response_class=JSONResponse)
async def health_check():
    return {"status": "ok", "message": "ML101 API is running"}
