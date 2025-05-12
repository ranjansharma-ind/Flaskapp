from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True)