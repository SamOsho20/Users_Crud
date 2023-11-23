from flask_app import app
from flask import render_template, request, redirect, session 

from flask_app.models.user import User
@app.route('/')
def index():
	return redirect('/users')
    # always want first app-route to be a redirect to our main page or login/registration page
@app.route('/users')
def users():
	
    return render_template("users.html", all_users = User.get_all())
    # when rendering template dont add / to beginging / only go to routes
    # this make our page pop up when its reloaded, also loading in 
    # all the users o they pop up on the page
        

@app.route('/user/create',methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
	
    return redirect ('/users')

@app.route('/user/new')
def new_user():
    return render_template ('new_user.html')
    # always render_template back to a page


@app.route('/show/user/<int:user_id>')
def show(user_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    user=User.get_by_id(user_id)
    return render_template("show.html", user = user)


@app.route('/update/user/<int:id>')
def edits(id):
    id=User.get_by_id(id)
    # calling the get_one method and supplying it with the id of the friend we want to get
    return render_template ('edit_user.html',id =id)

@app.route('/updated/user', methods=['POST'])
def update():
    User.update(request.form)
    # id=request.form
    print(request.form)
    #update method need data to run, the request.from takes input submitted at fill it in 
    # calling the get_one method and supplying it with the id of the friend we want to get
    return redirect ('/users')


@app.route('/delete/user/<int:user_id>')
def delete(user_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    User.delete(user_id)
    return redirect ('/users')
