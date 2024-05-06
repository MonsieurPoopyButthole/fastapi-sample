import logging
from starlette.requests import Request
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, Response
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import io  # For BytesIO
from src import helper
from typing import Dict, List
import os
from datetime import datetime, timezone
import sqlite3
from sqlite3 import Error


router = APIRouter()


def sql_connection():
    """ Create a connection with SQLite database specified
        by the mytest.db file
    :param con: the connection object
    :return: connection object or Error"""
    try:
        db = sqlite3.connect('books.db')
        return db
    except Error as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

#  060e29ee-f10e-4b56-896e-c73b54c02830
@router.get("/books", tags=["books"], name="get_books_collection")
async def get_books():
    connection = sql_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        items = [row for row in rows]

        return items

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
