#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/index/')
def test_xss():
    code = request.args.get('id')
    return render_template_string('<h2>Test flask xss！</h2><h3>{{code}}</h3>', code=code)

app.run()