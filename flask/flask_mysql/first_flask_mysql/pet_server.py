from flask import Flask, render_template, redirect, request
from mysqlconn import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('petshw')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("pets.html", pets = pets)

@app.route("/make_pets", methods=["POST"])
def add_pet_to_db():
    print(request.form)
    mysql = connectToMySQL('petshw')
    query = "INSERT INTO pets(name, type, created_at, updated_at) VALUES(%(n)s, %(t)s, NOW(), NOW());"
    data = {
        "n": request.form['pname'],
        "t": request.form['tname']
    }
    db = connectToMySQL('petshw')
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)