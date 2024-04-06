rom fastapi import APIRouter
from models.models import userM
from resolves.user import get_user,new_user,upd_user,del_user

user_router = APIRouter()

@user_router.get("/{id}")
def f_get_user(id:int):
    user = get_user(id)
    if user is None:
        return {"code":404,"message": "Пользователь с таким id: {id} не найден","user":None} #f
    return {"code":201,"message": "Успешно","user":user}

@user_router.post("/")
def f_new_user(user:userM):
    user = new_user(user)
    if user is None:
        return {"code":404,"message": "Ошибка","user":None}
    return {"code":201,"message": "Успешно","user":user}

@user_router.put("/{id}")
def f_upd_user(id:int,user:userM):
    user = upd_user(id,user)
    if user is None:
        return {"code":404,"message": "Пользователь с таким id: {id} не найден","user":None} #f
    return {"code":201,"message": "Успешно","user":user}

@user_router.put("/{id}")
def f_del_user(id:int):
    user = del_user(id)
    if user is None:
        return {"code":404,"message": "Пользователь с таким id: {id} не найден","user":None} #f
    return {"code":201,"message": "Успешно","user":user}