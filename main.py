import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename   #uploading file method of Flask
import cv2


UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    pass
    #image = cv2.imread(f"uploads/{filename}")


@app.route('/')
def starter():
    return render_template("webpage.html")


@app.route("/edit", methods = ["GET", "POST"] )
def edit():               
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No file error'
        file = request.files['file']
        operation = request.form['operation']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return 'No seleted file error'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f"Your file <a href= '/static/{filename}'> here </a> "

app.run(debug= True)




