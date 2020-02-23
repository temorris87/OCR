import os
import pytesseract
from flask import Flask, flash, make_response, request, redirect
from PIL import Image
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/mnt/c/Users/temor/Desktop/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

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
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename + '_test'))

        text = pytesseract.image_to_string(Image.open(file))
        response = make_response(str(text), 200)
        response.mimetype = "text/plain"
        return response


if __name__ == '__main__':
    application.run(debug=True)
