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
    image = cv2.imread(f"upload/{filename}")
    match operation:
        case "gray":
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            newFilename = f"static/{filename}"
            cv2.imwrite(newFilename, image_gray)
            return newFilename
        case "cjpg":
            newFilename = f"static/{filename.split('.')[0] + '.jpg'}"
            cv2.imwrite(newFilename, image)
            return newFilename
        case "cpng":
            newFilename = f"static/{filename.split('.')[0] + '.png'}"
            cv2.imwrite(newFilename, image)
            return newFilename
        case "cwebp":
            newFilename = f"static/{filename.split('.')[0] + '.webp'}"
            cv2.imwrite(newFilename, image)
            return newFilename
        
        


@app.route('/')
def starter():
    return render_template("webpage.html")



@app.route("/edit", methods = ["GET", "POST"])
def edit():               
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        operation = request.form['operation']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newFilename = processImage(filename, operation)
            return f"Your file <a href= '{newFilename}'> here </a> "
    return ''''''


app.run(debug= True)




