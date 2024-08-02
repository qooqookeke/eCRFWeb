from sqlalchemy import Boolean, Column, ForeignKey, INTEGER, VARCHAR, DATE, TIMESTAMP, FLOAT, DATETIME
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.database import Base
from datetime import datetime


# 계정 정보
class admin(Base):
    __tablename__ = "admin"
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True, unique=True)
    user_id = Column(VARCHAR(50), nullable=False)
    hased_pw = Column(VARCHAR(50), nullable=False)
    username = Column(VARCHAR(50), nullable=False)
    phone = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    created_at = Column(DATETIME, default=datetime.now)
    
    # 컬럼 간의 연결(ForeignKey)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # 속성과 연관된 다른 테이블의 속성값 연결
    # items = relationship("Item", back_populates="owner")

class guest(Base):
    __tablename__ = "guest"
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True, unique=True)
    p_id = Column(VARCHAR(50), nullable=False)
    hased_pw = Column(VARCHAR(50), nullable=False)
    created_at = Column(DATETIME, default=datetime.now)
    

# 대상자(환자) 정보
class p_info(Base):
    __tablename__ = "p_info"
    id = Column(INTEGER, nullable=False, autoincrement=True, primary_key=True, unique=True)
    initial = Column(VARCHAR(45), nullable=False)
    p_id = Column(VARCHAR(50), nullable=False)
    birth = Column(VARCHAR(10), nullable=False)
    sex = Column(TINYINT, nullable=False)
    weight = Column(FLOAT, nullable=False)
    height = Column(FLOAT, nullable=False)
    site = Column(TINYINT, nullable=False)
    op = Column(TINYINT, nullable=False)
    hx = Column(VARCHAR(100), nullable=False)
    smoke = Column(TINYINT, nullable=False)
    alcohol = Column(TINYINT, nullable=False)
    exercise = Column(TINYINT, nullable=False)
    created_at = Column(TIMESTAMP)
    
    def to_dict(self):
        return {
            "id": self.id,
            "initial": self.initial,
            "p_id": self.p_id,
            "birth": self.birth,
            "sex": self.sex,
            "weight": self.weight,
            "height": self.height,
            "site": self.site,
            "op": self.op,
            "hx": self.hx,
            "smoke": self.smoke,
            "alcohol": self.alcohol,
            "exercise": self.exercise,
            "created_at": self.created_at.isoformat(),
        }

    # items = relationship("Item", back_populates="owner")  # 데이터베이스간 연결 설정


# 설문 조사
class sv_womac(Base):
    __tablename__ = "sv_womac"
    code_id = Column(VARCHAR(50), primary_key=True, unique=True, nullable=False)
    fisrtcode = Column(VARCHAR(100))
    middle_code = Column(VARCHAR(100))
    lastcode = Column(VARCHAR(100))
    description = Column(VARCHAR(500))

class sv_koos(Base):
    __tablename__ = "sv_koos"
    code_id = Column(VARCHAR(50), primary_key=True, unique=True, nullable=False)
    fisrtcode = Column(VARCHAR(100))
    middle_code = Column(VARCHAR(100))
    lastcode = Column(VARCHAR(100))
    description = Column(VARCHAR(500))

class sv_ikdc(Base):
    __tablename__ = "sv_ikdc"
    code_id = Column(VARCHAR(50), primary_key=True, unique=True, nullable=False)
    fisrtcode = Column(VARCHAR(100))
    middle_code = Column(VARCHAR(100))
    lastcode = Column(VARCHAR(100))
    description = Column(VARCHAR(500))

class sv_ls(Base):
    __tablename__ = "sv_ls"
    code_id = Column(VARCHAR(50), primary_key=True, unique=True, nullable=False)
    fisrtcode = Column(VARCHAR(100))
    middle_code = Column(VARCHAR(100))
    lastcode = Column(VARCHAR(100))
    description = Column(VARCHAR(500))

class sv_etc(Base):
    __tablename__ = "sv_etc"
    code_id = Column(VARCHAR(50), primary_key=True, unique=True, nullable=False)
    fisrtcode = Column(VARCHAR(100))
    middle_code = Column(VARCHAR(100))
    lastcode = Column(VARCHAR(100))
    description = Column(VARCHAR(500))


# 설문 조사 결과
class result(Base):
    __tablename__ = "result"
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    p_id = Column(VARCHAR(50), ForeignKey("p_information.p_id"), nullable=False)
    visit = Column(TINYINT)
    code_id = Column(VARCHAR(50), nullable=False)
    score = Column(INTEGER)
    created_at = Column(TIMESTAMP)