from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'b99d74f05ed54e69b3a4d1e42cd0c9bfa8b83f1e75b942f394e2fd032cde3177'  
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)
