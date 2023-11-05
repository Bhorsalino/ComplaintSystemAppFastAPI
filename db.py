import databases
import sqlalchemy
from decouple import config


DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_NAME')}?sslmode=disable"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
