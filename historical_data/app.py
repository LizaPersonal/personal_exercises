from flask import Flask, render_template, flash, request, url_for, redirect
from werkzeug import secure_filename
import os
from file_reader import read_historical_data_file

ALLOWED_EXTENSIONS = set(['csv'])
UPLOAD_FOLDER = '/Users/lizajohn/Documents/Test'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config.from_object(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_historical_data():
    return render_template("import_data.html")


@app.route("/file", methods=["GET", "POST"])
def file_sample():
    if request.method == "POST":

        error = ""

        if 'raw_historical_data_csv' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['raw_historical_data_csv']
        if file.filename == '':
            error = "No file selected."
            return render_template("import_data.html", error=error)

        if not allowed_file(file.filename):
            error = "That file type is not allowed."
            return render_template("import_data.html", error=error)

        if file and allowed_file(file.filename):
            file_view = request.form
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            headers_after_reading, file_after_reading = read_historical_data_file(UPLOAD_FOLDER+'/'+filename)
            print(headers_after_reading)
            print(file_after_reading)
            return render_template("review_data.html", filename=filename, parameters=file_view, data=file_after_reading, headers=headers_after_reading)
            # return "The {} has been uploaded to {} for {}, based on the {} template" \
            #     .format(upload_file.filename, travel, client, tmc)

    return render_template("import_data.html", error=error)

        # tmc = request.form.get('tmc_name')
        # travel = request.form.get('travel_mode')
        # client = request.form['organization_name']
        #
        # print(file.filename)
        # print(tmc)
        # print(travel)
        # print(client)
        #
        # headers_after_reading, file_after_reading = read_historical_data_file('raw_historical_data_csv')
        # print(headers_after_reading)
        # print(file_after_reading)
        #


if __name__ == "__main__":
    app.run()
