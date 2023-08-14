from flask import Flask, render_template
import cv2

app = Flask(__name__, template_folder='template')

@app.route('/')
def memaybeo():
    return render_template("webpage.html")

app.run(debug= True)






