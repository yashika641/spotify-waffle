from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import session
from database import get_db
from models.user import user
from schemas.user import userout,userupdate
from auth import get_current_user

router = APIRouter(prefix='/me',tags=['user profile'])
@router.get('/',response_model=userout)
def get_user_profile(current_user: user = Depends(get_current_user)):
    return current_user

@router.put('/',response_model=userout)
def update_my_profile(
    update_data: userupdate,
    db: session = Depends(get_db),
    current_user: user = Depends(get_current_user)
):
    if update_data.full_name is not None:
        current_user.full_name =update_data.full_name
    if update_data.bio is not None:
        current_user.bio = update_data.bio
        
    db.commit()
    db.refresh(current_user)
    return current_user