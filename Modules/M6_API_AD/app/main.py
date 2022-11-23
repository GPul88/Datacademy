import fastapi

import sqlalchemy.orm as orm
import services, schemas

app = fastapi.FastAPI()

services.create_database()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: orm.Session=fastapi.Depends(services.get_db)):
    db_user = services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Whoops, the email is in already in use!")
    
    return services.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: orm.Session = fastapi.Depends(services.get_db)):
    users = services.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    db_user = services.get_user(db, user_id=user_id)
    if db_user is None:
        raise fastapi.HTTPException(status_code=404, detail="User not found!")
    return db_user


@app.post("/users/{user_id}/posts/", response_model=schemas.Article)
def create_article_for_user(user_id: int, article: schemas.ArticleCreate, 
                            db: orm.Session = fastapi.Depends(services.get_db)):
    db_user = services.get_user(db, user_id=user_id)
    if db_user is None:
        raise fastapi.HTTPException(status_code=404, detail="User not found!")
        
    return services.create_user_article(db=db, article=article, user_id=user_id)


@app.get("/posts/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: orm.Session = fastapi.Depends(services.get_db)):
    articles = services.get_articles(db, skip=skip, limit=limit)
    return articles


@app.get("/posts/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    db_article = services.get_article(db, article_id=article_id)
    if db_article is None:
        raise fastapi.HTTPException(status_code=404, detail="Article not found!")
    return db_article


@app.delete("/posts/{article_id}")
def delete_article(article_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    db_article = services.get_article(db, article_id=article_id)
    if db_article is None:
        raise fastapi.HTTPException(status_code=404, detail="Article not found!")
    
    services.delete_article(db, article_id=article_id)
    return {"message": f"Succesfully deleted article with id: {article_id}"}


@app.put("/posts/{article_id}")
def update_article(article_id: int, article: schemas.ArticleCreate, 
                   db: orm.Session = fastapi.Depends(services.get_db)):
    db_article = services.get_article(db, article_id=article_id)
    if db_article is None:
        raise fastapi.HTTPException(status_code=404, detail="Article not found!")
    
    return services.update_article(db, article=article, article_id=article_id)

