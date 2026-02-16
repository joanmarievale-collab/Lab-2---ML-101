from fastapi import HTTPException, Security, status

def verify_api_key(api_key: str = ""):
    if api_key != "mysecureapikey":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    return True
