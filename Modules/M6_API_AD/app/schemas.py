import datetime as dt
import pydantic


class _ArticleBase(pydantic.BaseModel):
    title: str
    content: str | None = None


class ArticleCreate(_ArticleBase):
    pass


class Article(_ArticleBase):
    id: int
    owner_id: int
    date_created: dt.datetime
    date_last_updated: dt.datetime

    class Config:
        orm_mode = True


class _UserBase(pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int 
    is_active: bool
    posts: list[Article] = [] 

    class Config:
        orm_mode = True  

