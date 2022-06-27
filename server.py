# FastAPI Sserver
"""Импортируем FastApi чтобы создать приложение"""
from urllib import response
from fastapi import FastAPI, Form
"""Импортируем response чтобы слать ответы в браузер
т.е. объект response инкапсулирует (установка внутри объекта
данных и каких то методов по обработке этих данных) 
в себе http ответ"""
from fastapi.responses import Response

# это ЭК приложения FasApi
app = FastAPI()

users = {
    'alexey@user.com': {
        'name': 'Алексей',
        'password': 'some_password_1',
        'balance': 100_000
    },
    'petr@user.com': {
        'name': 'Пётр',
        'password': 'some_password_2',
        'balance': 555_555
    }
}

# функция кот будет обрабатывать наш http запрос
@app.get('/')
def index_page():
    with open('templates/login.html', 'r') as r:
        login_page = r.read()
    return Response(login_page, media_type='text/html')

@app.post('/login')
def process_login_page(username : str = Form(...), password : str = Form(...)):
    user = users.get(username)
    if not user or user['password'] != password:
        return Response('Я вас не знаю', media_type='text/html')
    response = Response(
        f"Привет, {user['name']}! <br /> Баланс: {user['balance']}",
        media_type='text/html')
    response.set_cookie(key='username', value=username)
    return response





 
