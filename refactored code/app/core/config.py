import os

class Config:
    PROJECT_NAME: str = "ML101 Learning Lab"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ALLOWED_ORIGINS: list = ["*"]

config = Config()
