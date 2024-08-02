



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