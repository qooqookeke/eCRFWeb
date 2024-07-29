import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.model import p_info
from app.schemas import infoBaseCreate, infoBaseUpdate, sv_womac


# 환자 정보 생성
def create_pInfo(db: Session, pInfo_create: p_info):
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
		create_at=datetime.now()			
	)
	db.add(db_info)
	db.commit()
	db.refresh(db_info)
	return {"db_info": db_info}
	
# 전체 환자정보 리스트
def read_pInfo(db: Session, skip: int = 0, limit: int = 5):
	result = db.query(p_info).offset(skip).limit(limit).all()
	return result

# 특정 환자 정보
def read_pId(db: Session, p_id: str):
	result = db.query(p_info).filter(p_info.p_id == p_id).first()
	return result

# 특정 환자 정보 변경
def update_pId(db: Session, p_id: str, db_pInfo: p_info, pInfo_update: infoBaseUpdate):
	update_pInfo = db.query(p_info).filter(p_info.p_id == p_id).first()
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
	db.commit()


# 특정 환자 정보 삭제
def delete_pId(db: Session, p_id: str):
    db_pInfo = db.query(p_info).filter(p_info.id == p_id).first()
    if db_pInfo is None:
        raise HTTPException(status_code=404, detail="환자 정보를 찾을 수 없습니다.")
    db.delete(db_pInfo)
    db.commit()


# 관리자 등록

# 관리자 정보 수정

# 관리자 등록 삭제

# 관리자 로그인

# 관리자 로그아웃


# 게스트 등록

# 게스트 로그인

# 게스트 로그아웃


		


		# def update(self, db: Session, user_id: str, user: UsersUpdateItem):
		#     db_user = db.query(Users).filter(Users.user_id == user_id).update({
		#             Users.nickname: user.nickname,
		#             Users.email: user.email,
		#         }
		#     )
		#     db.commit()
		#     return db_user
		
		# def delete(self, db: Session, user_id: str):
		#     db_user = db.query(Users).filter(Users.user_id == user_id).first()
		#     db.delete(db_user)
		#     db.commit()
		#     return db_user