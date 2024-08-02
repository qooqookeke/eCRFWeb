from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model import p_info
from patient_info.info_schema import infoBase, infoBaseCreate, infoBaseUpdate

# 환자 고유 번호 중복 확인
async def get_existing_user(db: AsyncSession, p_id: str):
    async with db.begin():  # 세션을 시작합니다.
        result = await db.execute(select(p_info).filter(p_info.p_id == p_id))
        return result.scalars().first()

# 환자 정보 생성
async def create_pInfo(db: AsyncSession, pInfo_create: infoBaseCreate):
    db_info = p_info(
        initial=pInfo_create.initial,
        p_id=pInfo_create.p_id,
        birth=pInfo_create.birth,
        sex=pInfo_create.sex,
        weight=pInfo_create.weight,
        height=pInfo_create.height,
        site=pInfo_create.site,
        op=pInfo_create.op,
        hx=pInfo_create.hx,
        smoke=pInfo_create.smoke,
        alcohol=pInfo_create.alcohol,
        exercise=pInfo_create.exercise,
        created_at=datetime.now()
    )
    db.add(db_info)
    await db.commit()
    await db.refresh(db_info)
    return db_info


# 전체 환자정보 리스트
async def read_pInfo(db: AsyncSession):
    result = await db.execute(select(p_info).order_by(p_info.created_at.asc()))
    return result.scalars().all()


# 특정 환자 정보 조회
async def read_pId(db: AsyncSession, p_id: str):
    result = await db.execute(select(p_info).filter(p_info.p_id == p_id))
    return result.scalars().first()

# 특정 환자 정보 변경
async def update_pId(db: AsyncSession, p_id: str, pInfo_update: infoBaseUpdate):
    result = await db.execute(select(p_info).filter(p_info.p_id == p_id))
    db_pInfo = result.scalars().first()

    if db_pInfo is None:
        raise HTTPException(status_code=404, detail="환자 정보를 찾을 수 없습니다.")

    db_pInfo.p_id = pInfo_update.p_id
    db_pInfo.initial = pInfo_update.initial
    db_pInfo.birth = pInfo_update.birth
    db_pInfo.sex = pInfo_update.sex
    db_pInfo.weight = pInfo_update.weight
    db_pInfo.height = pInfo_update.height
    db_pInfo.site = pInfo_update.site
    db_pInfo.op = pInfo_update.op
    db_pInfo.hx = pInfo_update.hx
    db_pInfo.smoke = pInfo_update.smoke
    db_pInfo.alcohol = pInfo_update.alcohol
    db_pInfo.exercise = pInfo_update.exercise
    db.add(db_pInfo)
    await db.commit()
    return db_pInfo


# 특정 환자 정보 삭제
async def delete_pId(db: AsyncSession, p_id: str):
    result = await db.execute(select(p_info).filter(p_info.p_id == p_id))
    db_pInfo = result.scalars().first()
    await db.delete(db_pInfo)
    await db.commit()
    return db_pInfo
