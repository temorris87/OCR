import os
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\temor\\Desktop'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route('/')
def index():
    file = request.files['file']
    if file.filename == '':
        return 'Image not found.'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename + '_test'))
        return 'Image saved successfully.'


if __name__ == '__main__':
    application.run(debug=True)
