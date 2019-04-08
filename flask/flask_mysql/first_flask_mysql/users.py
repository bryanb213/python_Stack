from flask import Flask, render_template, redirect, request
from mysqlconn import connectToMySQL

app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('petshw')
    pets = mysql.query_db('SELECT * FROM users;')
    print(pets)
    return render_template("users_display.html", users = users)

@app.route("/make_pets", methods=["POST"])
def add_pet_to_db():
    print(request.form)
    mysql = connectToMySQL('User_form')
    query = "INSERT INTO user(first_name, last_name, email, created_at, updated_at) VALUES(%(n)s, %(t)s, NOW(), NOW());"
    data = {
        "n": request.form['pname'],
        "t": request.form['tname']
    }
    db = connectToMySQL('User_form')
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)