import string

from database.orm_query import orm_get_user_by_name, orm_get_admin_by_name


def user_in_db(user_name, user_password, session):
    user = orm_get_user_by_name(session, user_name)
    if user:
        print(user.password)
        if user.password == user_password:
            return True

    else:
        return False, ""


def admin_in_db(user_name, user_password, session):
    admin = orm_get_admin_by_name(session, user_name)
    if admin:
        print(admin.password)
        if admin.password == user_password:
            return True

    else:
        return False
