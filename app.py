from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import bcrypt  
from config import DATABASE_CONFIG

app = Flask(__name__)
# MySQL configurations
db = mysql.connector.connect(**DATABASE_CONFIG)
cursor = db.cursor()

cursor.execute("SELECT * FROM task ORDER BY id")
data = cursor.fetchall()
todo_list = data




@app.route('/')
def index():
 cursor.execute("SELECT * FROM task ORDER BY id")
 data = cursor.fetchall()
 
 return render_template('base.html',todo_list = data)

@app.route("/add",  methods=['POST'])
def add():
   activity = request.form.get("activity")
   
   
# Insert user data into the database
   insert_query = "INSERT INTO task (activity, complete) VALUES (%s, %s)"
   cursor.execute(insert_query, (activity,0))
   db.commit()
   return redirect(url_for("index"))

@app.route("/update/<int:task_id>")
def update(task_id):
    # Update task with the given ID in the database
    update_query = "UPDATE task SET complete = 1 WHERE id = %s"
    cursor.execute(update_query, (task_id,))
    db.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    # Delete task with the given ID from the database
    delete_query = "DELETE FROM task WHERE id = %s"
    cursor.execute(delete_query, (task_id,))
    db.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
