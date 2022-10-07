from fastapi import APIRouter

from models.users import userProfile, userProfileResponse

router = APIRouter()

@router.get("/{user_id}")
async def readUser(user_id: str):
    return {"user_id": user_id}

@router.post("/profile", response_model=userProfileResponse)
async def readUserProfile(model: userProfile):
    return model