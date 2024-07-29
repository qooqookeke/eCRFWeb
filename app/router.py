from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db, SessionLocal
from app.schemas import infoBase, infoBaseCreate, infoBaseUpdate, sv_womac, sv_koos, sv_ikdc, sv_ls, sv_etc, resultbase, result_msg
from app.crud import create_pInfo, read_pInfo, read_pId, update_pId, delete_pId
from app.model import p_info

router = APIRouter()


# 환자 정보 입력
@router.post("/patient/create", status_code=status.HTTP_201_CREATED)
def pInfo_create(_pInfo_create: infoBaseCreate, db: Session = Depends(get_db)):
    create_pInfo(db=db, create_pInfo=_pInfo_create)
    return result_msg(msg= f"환자 정보가 등록되었습니다.")

# 전체 환자 정보 리스트
@router.get("/patient/list")
def pInfo_list(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    db = SessionLocal()
    _pInfo_list = db.query(p_info).order_by(p_info.id.asc()).all()
    count = db.query(p_info).count()
    return {"data":_pInfo_list, "count":count}

# 특정 환자 정보
@router.get("/{user_id}")
def pId_get(p_id: str, db: Session = Depends(get_db)):
    db = SessionLocal()
    _pId_list = db.query(p_info).order_by(p_info.p_id(p_id))
    count = db.query(p_info).count()
    return {"data":_pId_list, "count":count}

# 특정 환자 정보 변경
@router.put("/update/{p_id}", status_code=status.HTTP_204_NO_CONTENT)
# current_admin: Admin = Depends(get_current_user) : 관리자 권한 수정
def pInfo_update(p_id: str, _pId_update: infoBaseUpdate, db: Session = Depends(get_db)):
    db_pId = update_pId(db, p_id = _pId_update.p_id)
    
    if not db_pId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    # if current_user.id != db_question.user.id:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail="수정 권한이 없습니다.")
    update_pId(db=db, db_pInfo=db_pId, update_pInfo=_pId_update)

    return result_msg(msg=f"환자 정보가 변경되었습니다.")

# 특정 환자 정보 삭제
@router.delete("/{p_id}", status_code=status.HTTP_204_NO_CONTENT)
# current_admin: User = Depends(get_current_user) : 관리자 권한 삭제
def pId_delete(p_id: str, _pId_delete: delete_pId, db: Session = Depends(get_db)):
    db_pId = delete_pId(db)

    if not db_pId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    # if current_user.id != db_question.user.id:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail="삭제 권한이 없습니다.")
    delete_pId(db=db, db_pInfo=db_pId)
    return result_msg(msg= "환자 정보를 삭제했습니다")