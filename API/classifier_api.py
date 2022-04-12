from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import flask, os, werkzeug
import json
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from PIL import Image
import predict_genre

app = Flask(__name__)
CORS(app)
api = Api(app)

UPLOAD_FOLDER = '/home/nickwood5/poster_classifier/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/ping', methods=['GET', 'POST'])
def aaaa():
    resp = flask.make_response(jsonify({"Poster API": "ONLINE"}))
    return resp

def get_filename():
    with open('/home/nickwood5/poster_classifier/counter.json') as json_file:
        data = json.load(json_file)
        data['upload_count'] += 1
        number = data['upload_count']

    with open('/home/nickwood5/poster_classifier/counter.json', 'w') as json_file:
        json.dump(data, json_file)

    return number

@app.route('/upload2', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        # check if the post request has the file part
        if 'file' not in request.files:
            return flask.make_response(jsonify({"Nick API": "5555?"}))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return flask.make_response(jsonify({"Nick API": "no selected file"}))
        if not allowed_file(file.filename):
            return flask.make_response(jsonify({"error": "bad_file_type"}))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.', 1)[1].lower()
            number = get_filename()
            filename = str(number) + '.' + extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = Image.open('/home/nickwood5/poster_classifier/uploads/' + filename)
            img = img.resize((182, 268), Image.LANCZOS)
            img = img.convert('RGB')
            img.save('/home/nickwood5/poster_classifier/cropped_uploads/' + str(number) + '.jpg')
            prediction = predict_genre.predict(str(number) + '.jpg')

            return flask.make_response(jsonify({"predictions": prediction}))
    return flask.make_response(jsonify({"Nick API": "works?"}))

if __name__ == "__main__":
    app.run(debug=True)