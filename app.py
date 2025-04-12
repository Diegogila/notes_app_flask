from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

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