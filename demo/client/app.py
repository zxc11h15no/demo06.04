from tkinter import *
import sqlite3
import os

def create_app(root,font,user_props):
    app = Toplevel(root)
    app.title("Ты в сети")
    app.geometry("1000x1000")
    l_main = Label(app,font=font, text="Ты в сети")
    l_main.grid(row=0,column=1)
    l_pacienti = Label(app,font=font, text="пациенты")
    l_pacienti.grid(row=1,column=1)
    #
    def insert_data(query,data):
        base_path = "db.db"
        connect = sqlite3.connect(base_path)
        cur = connect.cursor()
        res = cur.execute(query,data).fetchone() # кортеж
        connect.commit()
        connect.close()
        return res
    id = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    patronymic = StringVar()
    passport_number = StringVar()
    passport_series = StringVar()
    birth_date = StringVar()
    gender = StringVar()
    address = StringVar()
    phone_number = StringVar()
    email = StringVar()
    medical_card_number = StringVar()
    medical_card_issue_date = StringVar()
    last_visit_dat = StringVar()
    next_appointment_date = StringVar()
    insurance_policy_number = StringVar()
    insurance_policy_expiry_date = StringVar()


    # def get_users():
    #     l_main.config(text = "Ввести нужно все данные иначе будет ошибка. Сидеть вечно тут и обрабатывать каждую я не могу")
    #     users = insert_data("SELECT * FROM pacienti ",())
    #     if users is None:
    #         l_main.config(text = "Пользователей нет")
    #         return
    #     if(users):
    #         l_main.config(text = "Успешно")
    #         print(users)
    #         return
    #     l_main.config(text = "Ошибка")

    def get_user():
        l_main.config(text = "Введи необходимые данные")
        user = insert_data("SELECT * FROM pacienti WHERE id = ? ",(id.get()))
        print(user)
        if user is None:
            l_main.config(text = "Пользователь с таким id: {id} не найден")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            return
        l_main.config(text = "Ошибка")

    def new_user():
        fields = []
        values = []
        if(first_name is not None):
            fields.append("first_name")
            values.append(f"'{first_name}")
        if(last_name is not None):
            fields.append("last_name")
            values.append(f"'{last_name}")
        if(patronymic is not None):
            fields.append("patronymic")
            values.append(f"'{patronymic}")
        if(passport_number is not None):
            fields.append("passport_number")
            values.append(f"'{passport_number}")
        if( birth_date is not None):
            fields.append("birth_date")
            values.append(f"'{ birth_date}")
        if(gender is not None):
            fields.append("gender")
            values.append(f"'{gender}")
        if(address is not None):
            fields.append("address")
            values.append(f"'{address}")
        if(phone_number is not None):
            fields.append("phone_number")
            values.append(f"'{phone_number}")
        if(email is not None):
            fields.append("email")
            values.append(f"'{email}")
        if(password is not None):
            fields.append("password")
            values.append(f"'{password}")
        if( medical_card_number is not None):
            fields.append(" medical_card_number")
            values.append(f"'{ medical_card_number}")
        if(data_medic_card is not None):
            fields.append("data_medic_card")
            values.append(f"'{data_medic_card}")
        if(data_last_obrascheniya is not None):
            fields.append("data_last_obrascheniya")
            values.append(f"'{data_last_obrascheniya}")
        if(data_next_visit is not None):
            fields.append("data_next_visit")
            values.append(f"'{data_next_visit}")
        if(number_polis is not None):
            fields.append("number_polis")
            values.append(f"'{number_polis}")
        if(data_okonchaniya_polis is not None):
            fields.append("data_okonchaniya_polis")
            values.append(f"'{data_okonchaniya_polis}")
        if(role_id is not None):
            fields.append("role_id")
            values.append(f"'{role_id}")

        fields = ", ".join(fields)
        values = ", ".join(values)
        user = insert_data(f"""INSERT INTO pacienti ({fields}) VALUES ({values}) RETURNING id""",())
        print(user)
        if user is None:
            l_main.config(text = "Ошибка")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            create_app(app,font,user_props=user)
            return
        l_main.config(text = "Ошибка")

    def upd_user():
        l_main.config(text = "")

    def del_user():
        l_main.config(text = "Введи необходимые данные")
        user = insert_data("DELETE FROM pacienti WHERE id = ? RETURNING id",(id.get()))
        print(user)
        if user is None:
            l_main.config(text = "Пользователь с таким id: {id} не найден")
            return
        user_id = user[0]
        if(user_id):
            l_main.config(text = "Успешно")
            create_app(app,font,user_props=user)
            return
        l_main.config(text = "Ошибка")

    b_pacienti_get = Button(app,font=font, text="Получить пациента",command=get_user)
    # b_pacienti_gets = Button(app,font=font, text="Получить пациентов",command=get_users)
    b_pacienti_new = Button(app,font=font, text="Создать пациента",command=new_user)
    b_pacienti_upd = Button(app,font=font, text="Обновить пациента",command=upd_user)
    b_pacienti_del = Button(app,font=font, text="Удалить пациента",command=del_user)
    b_pacienti_get.grid(row=2,column=0)
    b_pacienti_gets.grid(row=2,column=4)
    b_pacienti_new.grid(row=2,column=1)
    b_pacienti_upd.grid(row=2,column=2)
    b_pacienti_del.grid(row=2,column=3)

    idl = Label(app,font=font, text="id")
    ide = Entry(app, textvariable=id,font=font)
    idl.grid(row=3,column=0)
    ide.grid(row=3,column=1)
    first_name = Label(app,font=font, text="first_name")
    first_name = Entry(app, textvariable=name,font=font)
    first_name.grid(row=4,column=0)
    first_name.grid(row=4,column=1)
    last_name = Label(app,font=font, text="last_name")
    last_name = Entry(app, textvariable=last_name,font=font)
    last_name.grid(row=5,column=0)
    last_name.grid(row=5,column=1)
    patronymic = Label(app,font=font, text="patronymic")
    patronymic= Entry(app, textvariable=patronymic,font=font)
    patronymic.grid(row=6,column=0)
    patronymic.grid(row=6,column=1)
    passport_number= Label(app,font=font, text="number_seria_pasport")
    passport_number= Entry(app, textvariable=number_seria_pasport,font=font)
    passport_number.grid(row=7,column=0)
    passport_number.grid(row=7,column=1)
    birth_date= Label(app,font=font, text=" birth_date")
    birth_date = Entry(app, textvariable= birth_date,font=font)
    birth_date.grid(row=8,column=0)
    birth_date.grid(row=8,column=1)
    gender = Label(app,font=font, text="gender")
    gender = Entry(app, textvariable=pol,font=font)
    gender.grid(row=9,column=0)
    gender.grid(row=9,column=1)
    addresse = Entry(app, textvariable=address,font=font)
    addressl = Label(app,font=font, text="address")
    addresse.grid(row=10,column=1)
    addressl.grid(row=10,column=0)
    phone_number= Entry(app, textvariable=phone_number,font=font)
    phone_number= Label(app,font=font, text="phone_number")
    phone_number.grid(row=11,column=1)
    phone_number.grid(row=11,column=0)
    emaill = Label(app,font=font, text="email")
    emaile = Entry(app, textvariable=email,font=font)
    emaill.grid(row=12,column=0)
    emaile.grid(row=12,column=1)
    passwordl = Label(app,font=font, text="password")
    passworde = Entry(app, textvariable=password,font=font)
    passwordl.grid(row=13,column=0)
    passworde.grid(row=13,column=1)
    medical_card_number = Label(app,font=font, text=" medical_card_number")
    medical_card_number = Entry(app, textvariable=number_medic_card,font=font)
    number_medic_cardl.grid(row=14,column=0)
    number_medic_carde.grid(row=14,column=1)
    data_medic_cardl = Label(app,font=font, text="data_medic_card")
    data_medic_carde = Entry(app, textvariable=data_medic_card,font=font)
    data_medic_cardl.grid(row=15,column=0)
    data_medic_carde.grid(row=15,column=1)
    data_last_obrascheniyal = Label(app,font=font, text="data_last_obrascheniya")
    data_last_obrascheniyae = Entry(app, textvariable=data_last_obrascheniya,font=font)
    data_last_obrascheniyal.grid(row=16,column=0)
    data_last_obrascheniyae.grid(row=16,column=1)
    data_next_visitl = Label(app,font=font, text="data_next_visit")
    data_next_visite = Entry(app, textvariable=data_next_visit,font=font)
    data_next_visitl.grid(row=17,column=0)
    data_next_visite.grid(row=17,column=1)
    number_polisl = Label(app,font=font, text="number_polis")
    number_polise = Entry(app, textvariable=number_polis,font=font)
    number_polisl.grid(row=18,column=0)
    number_polise.grid(row=18,column=1)
    data_okonchaniya_polisl = Label(app,font=font, text="data_okonchaniya_polis")
    data_okonchaniya_polise = Entry(app, textvariable=data_okonchaniya_polis,font=font)
    data_okonchaniya_polisl.grid(row=19,column=0)
    data_okonchaniya_polise.grid(row=19,column=1)
    role_idl = Label(app,font=font, text="role_id")
    role_ide = Entry(app, textvariable=role_id,font=font)
    role_idl.grid(row=20,column=0)