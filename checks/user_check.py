import datetime
import re
from email_validator import validate_email, EmailNotValidError

from sqlalchemy import select

from database.database import User
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


# check len all inputs
def validate_len_inputs(name, phone, email, service, master_name, date, time):
    if len(name) >= 2 and len(phone) >= 2 and len(email) >= 2 and len(service) >= 2 and len(master_name) >= 2 and len(
            str(date)) >= 2 and len(str(time)) >= 2:
        return True

    else:
        return False


# Check correct Name input
def validate_name_input(name):
    if not len(name) >= 2:
        reason = "Введите корректное имя"
        return False

    return True


# Check correct Phone input
def validate_phone_input(phone):
    phone_pattern = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'
    if re.match(phone_pattern, phone):
        print("MATCH PHONE")
        return True

    else:
        return False


# Check correct Email input
def validate_email_input(email):
    try:
        email = validate_email(email)
        email = email.normalized

        return email
    except EmailNotValidError as e:
        return None


# Check correct Date input
def validate_date_input(date_str):
    try:
        date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        return date

    except ValueError:
        return None


# Check correct Master Name
def validate_master_name_input(master_name):
    master_name_pattern = r'^\w+$'
    if re.match(master_name_pattern, master_name):
        return True
    else:
        return False


# Check correct Time input
def validate_time_input(time_str):
    try:
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        return time
    except ValueError:
        return None


# Time and date already in DB
def correct_time_date_master(session, date, time, master):
    query = select(User).filter(User.date == date, User.time == time, User.master == master)
    result = session.execute(query)
    existing_record = result.scalar()

    if existing_record:
        return False

    return True
