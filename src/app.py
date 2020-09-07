import os
import flask

from builder import Builder

#Create flask ppplication
app = flask.Flask(__name__)

#Define app entry point
@app.route('/', methods = ['POST'])
def run():

    #Define output directory
    outputDirectory = os.path.dirname(os.path.realpath(__file__)) + "/out/"

    #Build graph
    builder = Builder(flask.request.files['file'], flask.request.files['file'].filename, outputDirectory)
    valuePathFile = builder.build()

    return (flask.send_file(valuePathFile, attachment_filename = valuePathFile))

#Handle python entry points
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')