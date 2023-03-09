"""
 pip install fastapi
 pip install "fastapi[all]"
uvicorn main:app --reload
uvicorn blogging2:app --reload

"""

from typing import Optional
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel, Field
from uuid import UUID


##########################################################
# How to add a pydantic model and field validation?      #
##########################################################
class Blog(BaseModel):
    id: UUID  # unique identifier
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(
        title="description of blog",
        max_length=250,
        min_length=1
    )
    rating: int = Field(gt=-1, lt=101)

    # pre-defined request body example to appear in swagger
    class Config:
        schema_extra = {
            "example":
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "title": "Random Title",
                    "author": "Prashant",
                    "description": "This is a very interesting blog",
                    "rating": 75
                }
        }

class blogResponse(BaseModel):
    id : UUID
    title:str = Field(min_length=1)
    author: str
    description:Optional[str] = Field(
        None,
        title="description of blog",
        max_length=250,
        min_length=1
    )


class LanguageName(Enum):
    python = "Python"
    java = "Java"
    golang = "Golang"


app = FastAPI()

BLOGS = []


# V2 endpoints

def create_blogs_without_api():
    blog_1 = Blog(id="1a0b4e7e-bcd5-11ed-afa1-0242ac120002",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=50)
    blog_2 = Blog(id="1a0b499e-bcd5-11ed-afa1-0242ac120002",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=50)
    blog_3 = Blog(id="1a0b466e-bcd5-11ed-afa1-0242ac120002",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=50)
    blog_4 = Blog(id="1a0b477e-bcd5-11ed-afa1-0242ac120002",
                  title="Title 4",
                  author="Author 5",
                  description="Description 4",
                  rating=50)
    BLOGS.append(blog_1)
    BLOGS.append(blog_2)
    BLOGS.append(blog_3)
    BLOGS.append(blog_4)


##########################################################
# How to write a POST request with JSON request body?    #
##########################################################
@app.post("/v2/createblog")
def create_blog(blog: Blog):
    BLOGS.append(blog)
    return BLOGS


@app.get("/v2/")
def read_all_blogs(blogs_to_return: Optional[int] = None):
    if len(BLOGS) < 1:
        # create few blogs
        create_blogs_without_api()

    if blogs_to_return and blogs_to_return <= len(BLOGS):
        i = 1
        new_blogs = []
        while i <= blogs_to_return:
            new_blogs.append(BLOGS[i - 1])
            i += 1
        return new_blogs
    return BLOGS


