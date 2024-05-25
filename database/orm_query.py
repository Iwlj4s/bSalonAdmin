from sqlalchemy import select, delete, and_

from database.database import User
from database.database import Admin


# USERS stuff#

# ADD INFO IN REGISTRATION
def orm_user_add_info(session, data: dict):
    name = data.get("user_name")
    phone = data.get("user_phone")
    email = data.get("user_email")
    service = data.get("user_service")
    master = data.get("user_master")
    appointment_data = data.get("user_appointment_data")
    time = data.get("user_time")

    new_user = User(name=data.get("user_name"),
                    phone=data.get("user_phone"),
                    email=data.get("user_email"),
                    service=data.get("user_service"),
                    master=data.get("user_master"),
                    appointment_data=data.get("user_appointment_data"),
                    time=data.get("user_time"))

    session.add(new_user)
    session.commit()


# Get all users
def orm_get_users(session):
    query = select(User)
    result = session.execute(query)
    return result.scalars()


# Get one user by name
def orm_get_user_by_name(session, user_name):
    query = select(User).where(User.name == user_name)
    result = session.execute(query)
    user = result.scalar()

    return user


# Delete User
def orm_delete_user(session, name, phone, email, service, master, data, time):
    query = delete(User).where(and_(User.name == name, User.phone == phone, User.email == email,
                                    User.service == service, User.master == master,
                                    User.data == data, User.time == time))
    session.execute(query)
    session.commit()


# get admin by name
def orm_get_admin_by_name(session, user_name):
    query = select(Admin).where(Admin.name == user_name)
    result = session.execute(query)
    admin = result.scalar()

    return admin
