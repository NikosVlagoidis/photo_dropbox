import json
import os
from uuid import uuid4

from decouple import config
from flask import request, Blueprint, session, flash, url_for, render_template
from werkzeug.utils import secure_filename, redirect

from src.imgur_client import upload_image, get_photos


photo_blueprint = Blueprint('photos', __name__)


def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))


@photo_blueprint.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form
    
    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(uuid4())
    
    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True
    
    # Target folder for these uploads.
    target = ''#app.config['UPLOAD_FOLDER'] + "/{}".format(upload_key)
    try:
        os.mkdir(target)
    except:
        if is_ajax:
            return ajax_response(False,
                                 "Couldn't create upload directory: {}".format(
                                     target))
        else:
            return "Couldn't create upload directory: {}".format(target)
    
    for image_upload in request.files.getlist("file"):
        filename = secure_filename(image_upload.filename)
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        image_upload.save(destination)
        upload_image.delay(destination)
    
    if is_ajax:
        return ajax_response(True, upload_key)
    else:
        return redirect("/")


@photo_blueprint.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == config('PASSWORD') \
            and request.form['username'] == config('PDB_USERNAME'):
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect(url_for('photos.home_page'))


@photo_blueprint.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('photos.home_page'))


@photo_blueprint.route('/')
def home_page():
    if not session.get('logged_in'):
        return render_template('login.html')
    pics = [pic.link for pic in get_photos()]
    return render_template("homepage.html", pics=pics)
