from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded_file_url = None # URL of the uploaded file
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part in the form"
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            uploaded_file_url = filepath # path for display
    return render_template('index.html', uploaded_file_url=uploaded_file_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)