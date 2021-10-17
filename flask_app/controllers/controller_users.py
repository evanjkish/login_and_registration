from flask_app import app, bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models import model_user

@app.route('/logout')
def logout():
    session.pop('uuid')
    return redirect('/')

@app.route('/process_login', methods = ['POST'])
def new_user():
    is_valid = model_user.User.validate_login(request.form)

    if not is_valid:
        return redirect('/')
        return 'new user'

    potential_user = model_user.User.get_one_by_email({'email': request.form['email']})

    if not potential_user:
        return redirect('/')

    if not bcrypt.check_password_hash(potential_user.hash_pw, request.form['pw']):
        return redirect('/')

    session['uuid'] = potential_user.id
    return redirect('/dashboard')


@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = model_user.User.validate_registration(request.form)

    if not is_valid:
        return redirect('/')

    hash_pw = bcrypt.generate_password_hash(request.form['pw'])

    data = {
        **request.form,
        'hash_pw': hash_pw
    }

    user_id = model_user.User.create(data)

    session['uuid'] = user_id
    return redirect('/dashboard')

@app.route('/user/<int:id>')
def show_user(id):
    return 'show user'

@app.route('/user/<int:id>/edit')
def edit_user(id):
    return 'edit user'

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):
    return 'update user'

@app.route('/user/<int:id>/delete')
def delete_user(id):
    return 'delete user'