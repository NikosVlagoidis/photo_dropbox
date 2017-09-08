import os

from flask import render_template, request
from werkzeug.utils import secure_filename, redirect

from factory import create_app
from imgur_client import upload_image, get_photos

app = create_app()


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        upload_image.delay(file_path)
        return redirect('/')


@app.route('/')
def hello_world():
    pics = [pic.link for pic in get_photos()]
    return render_template("homepage.html", pics=pics)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
