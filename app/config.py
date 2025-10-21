import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST', '212.85.24.186')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'secretAnI@Ni1924')
    DB_NAME = os.getenv('DB_NAME', 'CDatabase')
    DB_PORT = os.getenv('DB_PORT', 3306)
