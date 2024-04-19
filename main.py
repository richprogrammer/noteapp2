from flask import Flask, render_template, request, url_for

#Creating the app
app = Flask(__name__)

#Creating the main page
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        webpage = request.form
        notes_inp = str(webpage['notesInp'])
        print(notes_inp)

    return render_template("index.html")

#Running the app
if __name__ == '__main__':
    app.run(debug=True)