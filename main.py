from flask import Flask
from data import db_session
from data.users import User

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.name = "Ridley"
    user.surname = 'Scott'
    user.age = 21
    user.position = 'captain'
    user.speciality = "research engineer"
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"

    user2 = User()
    user2.name = "Ridley2"
    user2.surname = 'Scott'
    user2.age = 21
    user2.position = 'captain'
    user2.speciality = "research engineer"
    user2.address = 'module_1'
    user2.email = "scott2_chief@mars.org"

    user3 = User()
    user3.name = "Ridley3"
    user3.surname = 'Scott'
    user3.age = 21
    user3.position = 'captain'
    user3.speciality = "research engineer"
    user3.address = 'module_1'
    user3.email = "scott3_chief@mars.org"

    user4 = User()
    user4.name = "Ridley4"
    user4.surname = 'Scott'
    user4.age = 21
    user4.position = 'captain'
    user4.speciality = "research engineer"
    user4.address = 'module_1'
    user4.email = "scott4_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(user4)
    db_sess.commit()
#    app.run()


if __name__ == '__main__':
    main()