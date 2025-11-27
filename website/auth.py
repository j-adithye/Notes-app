from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")
        pass
    return render_template("login.html", text = "testing")


@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password1')
        
        if len(email)<4:
            flash("email len 4+", category='error')
        else:
            #add user to db
            new_user = User(email = email, first_name=first_name, last_name = last_name,password = generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category='success')
            return redirect(url_for('views.home'))
            
        
        
        
    if request.method == "POST":
        pass
    return render_template("signup.html")




@auth.route('/logout')
def logout():
    return "logout"