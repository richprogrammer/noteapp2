from flask import Flask, render_template, request, url_for

#Creating the app
app = Flask(__name__)

#Creating the main page
def main():
    return render_template()

#Running the app
if __name__ == '__main__':
    app.run(debug=True)