from flask import Flask, render_template, send_file, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/portfolio'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Uservalue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.String(50), unique=False)
    
@app.route('/', methods=['GET', 'POST'])
def home():
    email = request.form.get('email')
    if email:
        try:
            entry = Uservalue(email=email, date=datetime.now())
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return "Email already exists in the database."
    else:
        return render_template ('index.html')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    # Replace 'resume.pdf' with the actual path to your resume file
    return send_file('static/RanjanCV.pdf', as_attachment=True)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)