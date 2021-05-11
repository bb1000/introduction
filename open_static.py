#!/usr/bin/env python

import flask
import random
import pathlib

root = pathlib.Path(__file__).parent.resolve()
app = flask.Flask(__name__, static_folder=root, static_url_path='/introduction', template_folder=root)


@app.route('/')
def index():
    return flask.render_template('index.html')


port = int(5000 + 5000*random.random())
app.run(debug=True, port=port)
