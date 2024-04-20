from flask import Flask, render_template, request, url_for

#Creating the app
app = Flask(__name__)

#Global Variables
notes_list = []

#Creating the main page
@app.route("/", methods=["GET", "POST"])
def main():
    global notes_list

    if request.method == "POST":
        webpage = request.form
        notes_inp = str(webpage['notesInp'])
        print(notes_inp)
        notes_list.append(notes_inp)

    return render_template("index.html")

#Running the app
if __name__ == '__main__':
    app.run(debug=True)