import datetime
import string

from database.orm_query import orm_get_user_by_name, orm_get_admin_by_name, orm_get_user_date, orm_get_user_time, \
    orm_get_master


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


# Check correct Date input
def validate_date_input(date_str):
    try:
        date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        return date

    except ValueError:
        return None


# Check correct Time input
def validate_time_input(time_str):
    try:
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        return time
    except ValueError:
        return None


# Time and date already in DB
def correct_time_date_master(session, date, time, master):
    date = orm_get_user_date(session=session, date=date)
    time = orm_get_user_time(session=session, time=time)
    master = orm_get_master(session=session, master=master)
    reason = "В этот день на это время к этому мастеру уже есть запись"

    if date and time:
        return False, reason

    return True, ""
