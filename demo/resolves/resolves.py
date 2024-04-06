from base import insert_data
from models.models import userM

def get_user(id:int):
    user = insert_data(f"select * from users where id = {id}")
    if user is None:
        return None
    user = {"id": user[0],}
    return user

def new_user(user:userM):
    fields = []
    values = []
    # user = insert_data(f"select * from users where id = {id}")
    # if user is None:
    #     return None
    # user = {"id": user[0],}
    # return user
    return None

def upd_user():
    return None

def del_user():
    return None