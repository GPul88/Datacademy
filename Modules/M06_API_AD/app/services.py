import sqlalchemy.orm as orm
import database, models, schemas

import datetime as dt

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: orm.Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: orm.Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "thisisnotsecure"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all() 

def get_user(db: orm.Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user_article(db: orm.Session, article: schemas.ArticleCreate, user_id: int):
    db_article = models.Article(**article.dict(), owner_id=user_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_articles(db: orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Article).offset(skip).limit(limit).all()

def get_article(db: orm.Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def delete_article(db: orm.Session, article_id: int):
    db.query(models.Article).filter(models.Article.id == article_id).delete()
    db.commit()

def update_article(db: orm.Session, article: schemas.ArticleCreate, article_id: int):
    db_article = get_article(db=db, article_id=article_id)
    db_article.title = article.title
    db_article.content = article.content
    db_article.date_last_updated = dt.datetime.now()
    db.commit()
    db.refresh(db_article)
    return db_article

