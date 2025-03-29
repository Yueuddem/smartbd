# smartbd

가상환경만들고 
pip install -r requirements.txt
라이브러리설치

settings.py 파일에 데이터베이스 맞춰주고 postgres 깔려있어야함
DATABASES = {
    }
여기서 안에 있는 내용 바꿔줘야됨


bash에서 모델 만들어주는 명령어 
python manage.py makemigrations

                     
python manage.py migrate

서버실행
python manage.py runserver

