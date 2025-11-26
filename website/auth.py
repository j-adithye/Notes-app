from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    data = request.form
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
        if len(first_name)<2:
            pass
        else:
            #add user to db
            flash("Account Created", category='success')
            pass
        
        
        
    if request.method == "POST":
        pass
    return render_template("signup.html")




@auth.route('/logout')
def logout():
    return "logout"