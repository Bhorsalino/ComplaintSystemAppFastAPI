from typing import List, Optional
from fastapi import APIRouter, Depends
from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from schemas.response.user import UserOut
from models.enums import RoleType


router = APIRouter(tags=["Users"])

@router.get("/users/", response_model=List[UserOut], dependencies=[Depends(oauth2_scheme), Depends(is_admin)])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()


@router.put("/users/{user_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_rol(RoleType.admin, user_id)


@router.put("/users/{user_id}/make-approver", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_rol(RoleType.approver, user_id)
