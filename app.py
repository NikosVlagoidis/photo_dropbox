import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, redirect

from imgur_client import upload_image

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        res = upload_image(file_path)
        print(res['link'])
        return redirect('/')


@app.route('/')
def hello_world():
    pics = os.listdir(UPLOAD_FOLDER)
    return render_template("homepage.html", pics=pics)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
