from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'notes.sqlite'
)

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    create_note = db.Column(db.DateTime, default=datetime.utonow)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"


@app.route('/')
def hello():
    role="Admin"
    notes = ['Nota 1','Nota 2', 'Nota 3']
    return render_template('home.html',role=role, notes=notes)

@app.route('/aboutus')
def about():
    return 'This is an app of notes'

@app.route('/contactus',methods=['POST','GET'])
def contactUs():
    if request.method == "POST":
        return "Form sended sucefully", 201
    return 'Contact Page'

@app.route('/api/info')
def api_info():
    data = {
        "name":"Notes App",
        "version" : "1.1.1"
    }
    return jsonify(data), 200

@app.route('/confirmation')
def confirmation():
    return 'Prueba'

@app.route('/create-note', methods=['GET','POST'])
def create_note():
    if request.method == 'POST':
        note = request.form.get('note',"Not found")
        return redirect(
            url_for('confirmation', note=note)
        )
    return render_template('note_form.html')