import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BD_HOST = os.environ.get("BD_HOST")
BD_NAME = os.environ.get("BD_NAME")
BD_PORT = os.environ.get("BD_PORT")
BD_USER = os.environ.get("BD_USER")
BD_PASSWORD = os.environ.get("BD_PASSWORD")

SECRET_KEY = os.environ.get("SECRET_KEY")
