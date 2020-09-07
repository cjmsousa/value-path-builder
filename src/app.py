import flask

#Create flask ppplication
app = flask.Flask(__name__)

#Define app entry point
@app.route('/')
def home():

    return 'App Home Page'

#Start flask app if run from commandline
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')


