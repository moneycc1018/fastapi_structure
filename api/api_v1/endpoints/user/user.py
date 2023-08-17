from fastapi import APIRouter

from schemas.user import userProfile, userProfileResponse
import config

router = APIRouter()

@router.get("/{user_id}")
async def readUser(user_id: str):
    test_env_var = config.TEST
    return {"user_id": user_id, "test_env_var": test_env_var}

@router.post("/profile", response_model=userProfileResponse)
async def readUserProfile(model: userProfile):
    return model