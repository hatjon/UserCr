from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')



@app.route('/users')
def users():
    allUsers = User.get_all()
    return render_template('users.html', users= allUsers )

@app.route('/add/user')
def createForm():
    return render_template('createUser.html')


@app.route('/create/user', methods=['POST'])
def createUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')


