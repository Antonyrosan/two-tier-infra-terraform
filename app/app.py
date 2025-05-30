from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # add your MySQL password
    database="student_db"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        cursor.execute("INSERT INTO students (name, age, department) VALUES (%s, %s, %s)", (name, age, dept))
        db.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        cursor.execute("UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s", (name, age, dept, id))
        db.commit()
        return redirect('/')
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
