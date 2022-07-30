from email import message
from time import timezone
from flask import Flask, render_template, request
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:actecal2020@localhost/intern_22'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name= db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100))
    subject=db.Column(db.String(100), nullable=False)
    message=db.Column(db.String(255), nullable=False)
    # created_at=db.column(db.DateTime(timezone=True), server_default=func.now())


# TypeError: The view function did not return a valid response. \
# The return type must be a string, dict, tuple, Response instance, or WSGI\
#  callable, but it was a int.

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact', methods=["POST","GET"])
def contact():
    if request.method== "POST":
        Name = request.form.get('name')
        Email=request.form.get('email')
        Subject=request.form.get('subject')
        Message=request.form.get('message')
        contact_data=Contact(id =1,name=Name,email=Email,subject=Subject,message=Message)
        db.session.add(contact_data)
        db.session.commit()
        return render_template("home.html")
    return render_template("contact.html")

@app.route('/register')
def register():
    return render_template("register.html")
    


if __name__ == "__main__":
    db.create_all()
    app.run(port=3000, debug=True)
