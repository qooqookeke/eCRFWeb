from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from app.database import get_db, AsyncSessionLocal
from app.model import p_info
from patient_info.info_schema import infoBase, infoBaseCreate, PInfoResponse, infoBaseUpdate
from patient_info.info_crud import get_existing_user, create_pInfo, read_pInfo, read_pId, update_pId, delete_pId

router = APIRouter(prefix="/patient", tags=['p_info'])


# 환자 정보 입력
@router.post("/create")
async def pInfo_create(body: infoBaseCreate, db: AsyncSession = Depends(get_db)):
    # male = 0, female = 1 / site R = 0, L = 1
    # op : 수술명,  hx : 과거 병력
    existing_user = await get_existing_user(db, body.p_id)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    await create_pInfo(db=db, pInfo_create=body)
    return {'msg': f"환자 정보가 등록되었습니다."}


# 전체 환자 정보 리스트
@router.get("/list", response_model=PInfoResponse)
async def pInfo_list(db: AsyncSession = Depends(get_db)):
    items = await read_pInfo(db)  
    data_list = []
    for item in items:
        data_list.append(infoBase(
            initial=item.initial,
            p_id=item.p_id,
            birth=item.birth,
            sex=item.sex,
            weight=item.weight,
            height=item.height,
            site=item.site,
            op=item.op,
            hx=item.hx,
            smoke=item.smoke,
            alcohol=item.alcohol,
            exercise=item.exercise
        ))
    count_stmt = select(func.count()).select_from(p_info)
    count_result = await db.execute(count_stmt)
    count = count_result.scalar()
    
    return PInfoResponse(data=data_list, count=count)


# 특정 환자 정보 조회
@router.get("/{p_id}")
async def pId_get(p_id: str, db: AsyncSession = Depends(get_db)):
    result = await read_pId(db, p_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="환자 정보를 찾을 수 없습니다.")
    return result


# 특정 환자 정보 변경
@router.put("/update/{p_id}/")
async def pInfo_update(p_id: str, pId_update: infoBaseUpdate, db: AsyncSession = Depends(get_db)):
# def question_update(pId_update: infoBaseUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):

    db_pId = await read_pId(db, p_id)
    if not db_pId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="데이터를 찾을 수 없습니다.")
    # if current_user.id != db_question.user.id:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail="수정 권한이 없습니다.")
    await update_pId(db=db, p_id=p_id, pInfo_update=pId_update)
    return {'msg': "환자 정보가 변경되었습니다."}


# 특정 환자 정보 삭제
@router.delete("/delete/{p_id}/")
async def pId_delete(p_id: str, db: AsyncSession = Depends(get_db)):
    db_pId = await read_pId(db, p_id)
    if not db_pId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="환자 정보를 찾을 수 없습니다.")
    # 권한 확인 로직 (주석 처리된 부분을 수정)
    # if current_user.id != db_pId.user_id:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail="삭제 권한이 없습니다.")
    await delete_pId(db=db, p_id=p_id)
    return {'msg': "환자 정보를 삭제했습니다"}