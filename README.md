docker run -d \
    --name complaint_db \
    --env-file .env \
    -v /home/jpallares/GitHub/Python-General/ComplaintSystemApp/data:/var/lib/postgresql/data \
    -p 5434:5432 \
    postgres:latest

alembic init migrations
alembic revision --autogenerate -m "Add phone"
alembic upgrade head

To create admin User:
export PYTHONPATH=./
python commands/create_super_user.py -f George -l Pallares -e admin@admin.com -p 12345678 -i GB29NWBK60161331926819 -pa 123


Todos los passwords son: 123
