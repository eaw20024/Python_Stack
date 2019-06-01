from flask import Flask, render_template, request, redirect
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/users/new")
def new():
    return render_template("new.html")


@app.route("/create_users", methods=["POST"])
def add_users_to_db():
    # print(request.form)
    mysql = connectToMySQL("users")

    query = "INSERT INTO users (full_name, email, created_at, updated_at) VALUES (%(fnm)s, %(email)s, NOW(), NOW());"
    data = {
        "fnm": request.form["full_name"],
        "email": request.form["email"]
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect(f"/user/{new_friend_id}")


@app.route('/user/<id>')
def user_display(id):
    # print(id)
    mysql = connectToMySQL("users")
    query = f"SELECT * FROM users.users WHERE id = {id};"
    user_list = mysql.query_db(query)
    # print(user_list)
    return render_template("user_display.html", user_list=user_list)


@app.route('/users/<id>/edit')
def edit_user(id):
    mysql = connectToMySQL("users")
    query = f"SELECT * FROM users.users WHERE id = {id};"
    user_list = mysql.query_db(query)
    # print(user_list)
    return render_template("edit_user.html", user_list=user_list)


@app.route('/update_user/<int:id>', methods=["POST"])
def update_user(id):
    mysql = connectToMySQL("users")
    data = {
        'full_name': request.form['full_name'],
        'email': request.form['email']
    }
    # print(id)
    query = f"UPDATE `users`.`users` SET full_name=%(full_name)s, email=%(email)s, updated_at=NOW() WHERE id={id} LIMIT 1;"
    mysql.query_db(query, data)
    return redirect(f"/user/{id}")


@app.route('/show_users')
def show_users():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM users.users;')
    return render_template('users.html', all_users=users, users=users)


@app.route('/users/<id>/delete')
def delete(id):
    mysql = connectToMySQL('users')
    query = f"DELETE FROM `users`.`users` WHERE id = {id}"
    user_list = mysql.query_db(query)
    return redirect("/show_users")


if __name__ == "__main__":
    app.run(debug=True)
