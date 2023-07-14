from data.bot_config import TOKEN, ADMIN
from data.database_config import DB_NAME, DB_USER, DB_HOST, DB_PORT, DB_PASSWORD
from data.refill_config import UKASSA_TOKEN

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"