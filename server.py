from flask import Flask, render_template, redirect, request, session
from user import User

app = Flask(__name__)

@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/users/new')
def show_form():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)