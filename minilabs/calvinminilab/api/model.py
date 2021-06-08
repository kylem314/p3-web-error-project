from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from flask_restful import Resource, Api

from model import app

dbURI = 'sqlite:///model/myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)

Migrate(app, db)
api = Api(app)
url_prefix = "/crud"


# declare the users database model
class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # self variables
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    # json/dictionary converter
    def json(self):
        return {
            "userID": self.userID,
            "username": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

    # class for create/post
    class Create(Resource):
        def post(self, name, email, password, phone):
            person = model_create(name, email, password, phone)
            if person:
                return person.json()
            return {'email': None}, 404  # need to have better message on errors

    # class for read/get
    class Read(Resource):
        def get(self):
            return model_read_all()

    # class for update/put
    class Update(Resource):
        def put(self, email, name):
            user = model_read_email(email)
            if user is None:
                return None
            model_update_name({'userid': user['userID'], 'name': name})
            return None  # needs error handling

    # class for delete
    class Delete(Resource):
        def delete(self, userid):
            model_delete(userid)

    # building RESTapi resource
    api.add_resource(Create, url_prefix + '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(Read, url_prefix + '/read/')
    api.add_resource(Update, url_prefix + '/update/<string:email>/<string:name>')
    api.add_resource(Delete, url_prefix + '/delete/<int:userid>')


# CRUD create/add a new record to the table
# user_dict{} expects name, email, password, phone; returns person object on success
def model_create(name, email, password, phone):
    """prepare data for primary table extracting from form"""
    try:
        person = Users(
            name=name,
            email=email,
            password=password,
            phone=phone
        )
        db.session.add(person)
        db.session.commit()
        return person
    except:
        return None


# CRUD read: filter single record in table based off of userid
# userid required, returns json/dictionary
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(userID=userid).first()
    return user.json()


# CRUD read: filter single record in table based off of email
# userid required, returns json/dictionary
def model_read_email(email):
    """filter users by userid"""
    user = Users.query.filter_by(email=email).first()
    if user is None:
        return None
    return user.json()


# CRUD update: updates users name
# requires userid, returns json/dictionary
def model_update_name(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    user = Users.query.filter_by(userID=userid).first()
    if user is None:
        return None
    db.session.query(Users).filter_by(userID=userid).update({Users.name: user_dict['username']})
    """commit changes to database"""
    db.session.commit()
    return user.json()


# CRUD delete: removes record from table
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    db.session.query(Users).filter(Users.userID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_read_all():
    """convert Users table into a list of dictionary rows"""
    people = Users.query.all()
    return [peep.json() for peep in people]


# CRUD read: query emails
def model_read_emails():
    # fill the table with emails only
    people = Users.query.all()
    return [{'userID': peep.userID, 'email': peep.email} for peep in people]


# CRUD read: query phones
def model_read_phones():
    # fill the table with phone numbers only
    people = Users.query.all()
    return [{'userID': peep.userID, 'phone': peep.phone} for peep in people]


#### testing section
# create database from scratch
def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='123toby', phone="1111111111")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")
    record = model_read_email('jmort1021@yahoo.com')
    print()
    print("New Email Method", record['userID'], record['email'], record['name'])


# simple listing of table
def print_tester():
    print("------------")
    print("Table: users")
    print("------------")
    result = model_read_all()
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    print_tester()