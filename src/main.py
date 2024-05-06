from fastapi import FastAPI
import os
import logging  # For logging
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles # For environment variables
from src import router
from fastapi.middleware.cors import CORSMiddleware
from src.api_spec import api_spec_editor
from src import helper

# Initialize environment and logging
path_to_env_file = helper.get_root_path() + "/.env"
load_dotenv(path_to_env_file)
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
logging.basicConfig(level=LOG_LEVEL.upper())



app = FastAPI()


######################----------ROUTES
app.include_router(router.api_router)
######################----------ROUTES


######################----------DOCS
app.openapi_schema = api_spec_editor.set_openapi_spec(app.openapi_schema, app.routes)
######################----------DOCS


# app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def get_homepage():
    return {"Response": "This is the home page"}

