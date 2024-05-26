from database.orm_query import orm_get_users


def get_users_list(session):
    users_info = ""
    for user in orm_get_users(session=session):
        user_name = user.name
        user_phone = user.phone
        user_email = user.email
        user_service = user.service
        user_master = user.master
        user_date = user.date
        user_time = user.time
        user_info = (f"Имя: {user_name}, Телефон: {user_phone}, Почта: {user_email},"
                     f" Услуга: {user_service}, Мастер: {user_master}, Дата: {user_date}, Время-{user_time}")
        users_info += user_info + "\n"

    print(users_info)
    return users_info


def count_list_items(session):
    counter = 0
    for user in orm_get_users(session=session):
        counter += 1

    return str(counter)
