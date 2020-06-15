# -*- coding:utf8 -*-
# !/usr/bin/env python
import logging

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    port = 14000
    logging.debug("Starting app on port %d" % port)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
