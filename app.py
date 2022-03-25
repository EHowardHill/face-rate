import os, random, datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://ethan:Shebang01#!@face-server.database.windows.net:1433/db?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Records(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    voter_id = db.Column(db.Integer)
    photo_id = db.Column(db.Integer)
    age = db.Column(db.Integer)
    likes_men = db.Column(db.Integer)
    likes_women = db.Column(db.Integer)

def random_photo():
    files = os.listdir("./static")
    return(random.choice(files))

@app.route('/')
def hello(name=None):
    print(random_photo())
    return render_template('index.html',
    leftPic=random_photo(),
    rightPic=random_photo())

@app.route('/submit', methods=['GET','POST'])
def submit():

    success = False
    error = ''

    try:
        id = int(request.form.get("photo")[8:].replace('/static/', '').replace('.jpg', ''))

        newEntry = Records(
            created_at = datetime.datetime.now(),
            voter_id = int(request.form.get("id")),
            photo_id = id,
            age = int(request.form.get("age") if request.form.get("age") != '' else 0),
            likes_men = True if request.form.get("men") == "true" else False,
            likes_women = True if request.form.get("women") == "true" else False
            )

        db.session.add(newEntry)
        db.session.commit()

        success = True

    except Exception as e:
        success = False
        error = str(e)
        success = False

    return(
        {
            "valid": success,
            "src1": '/static/' + random_photo(),
            "src2": '/static/' + random_photo(),
            "error": error
        })