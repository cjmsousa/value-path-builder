import os
import flask

from builder import Builder

#Create flask ppplication
app = flask.Flask(__name__)

#Define app entry point
@app.route('/', methods = ['POST'])
def run():

    #Build graph
    builder = Builder(flask.request.files['file'], flask.request.files['file'].filename)
    valuePathFile = builder.build()

    return (flask.send_file(valuePathFile))

#Handle python entry points
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')