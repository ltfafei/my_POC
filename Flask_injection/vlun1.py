#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/index/')
def test_xss():
    code = request.args.get('id')
    html = '''
        <h2>Test flask xss！</h2>
        <h3>%s</h3>
    '''%(code)
    return render_template_string(html)

app.run()