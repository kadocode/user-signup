from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup', methods = ['POST', 'GET'])
def display_signup_form():
    if request.method == 'POST':
        username = request.form['username']
        password =request.form['password']
        verify =request.form['verify']
        email =request.form['email']
        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ''
        if len(username) < 3 or len(username) > 20 or " " in username:
            username_error = "Username Not Valid"
        if len(password) < 3 or len(password) > 20 or " " in password:
            password_error = "Password Not Valid"
        if password != verify:
            verify_error = "Passwords Do Not Match"
        if email:
            if '@' not in email or '.' not in email:
                email_error = "Email Not Valid"
        if username_error or password_error or verify_error or email_error:
            return render_template("base.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

        if not username_error or not password_error or not verify_error or not email_error:
            return redirect("/loggedin?username={0}".format(username))
    return render_template("base.html")
    
@app.route('/loggedin')
def login():
    username = request.args.get('username')

    return('<h1>Thanks for signing up, ' + username + '</h1>')


app.run()