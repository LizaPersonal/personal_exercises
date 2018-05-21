from flask import Flask, render_template, flash, request, url_for, redirect

ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
# app.config.from_object(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_historical_data():

    error = ""

    try:
        if request.method == "POST":

            upload_file = request.files['raw_historical_data_csv']
            tmc = request.form.get('tmc_name')
            travel = request.form.get('travel_mode')
            client = request.form['organization_name']

            if upload_file.filename == '':
                error = "No file selected."
                return render_template("import_data.html", error=error)

            elif upload_file and allowed_file(upload_file.filename):
                print(upload_file.filename)
                print(tmc)
                print(travel)
                print(client)
                return "The {} has been uploaded to {} for {}, based on the {} template" \
                    .format(upload_file.filename, travel, client, tmc)

            elif not allowed_file(upload_file.filename):
                error = "That file type is not allowed."
                return render_template("import_data.html", error=error)

        return render_template("import_data.html")

    except Exception as e:
        print(e)
        return render_template("import_data.html", error=error)


if __name__ == "__main__":
    app.run()
