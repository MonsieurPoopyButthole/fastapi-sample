from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel, field_validator, ValidationError, Field
from src import helper
from datetime import datetime
import sqlite3
from sqlite3 import Error
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()


class Book(BaseModel):
    name: str
    author: str = Field(max_length=40)
    year: str
    description: str
    logo: str

    @field_validator("year")
    def validate_date_format(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        return value


def sql_connection():
    """Create a connection with SQLite database specified
        by the mytest.db file
    :param con: the connection object
    :return: connection object or Error"""
    try:
        db = sqlite3.connect("books.db")
        return db
    except Error as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}


#  060e29ee-f10e-4b56-896e-c73b54c02830
@router.get("/books", tags=["books"], name="get_books_collection")
async def get_books(request: Request):
    templates = Jinja2Templates(directory=helper.get_root_path() + "/src/templates")
    connection = sql_connection()
    # connection.row_factory = sqlite3.Row
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        # items = {vars(row) for row in rows}

        rendered_values = {"request": request, "data": rows}
        return templates.TemplateResponse("index.html", rendered_values)

    except Error as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/books", tags=["books"], name="get_books_collection")
async def add_books(request: Book):
    query = """INSERT INTO books (name, author, year, description, logo) VALUES(?,?,?,?,?)"""
    book_values = [val for key, val in request.model_dump().items()]
    connection = sql_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, book_values)
        connection.commit()
        print("The record added successfully")
        return JSONResponse("Resource Created", 201)
    except Error as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}


# @router.get("/articles", tags=["articles"], name="get_article_collection")
# async def get_article():
#     try:
#         return {"yeet"}
#     except Exception as e:
#         return {"success": False, "error": str(e)}
