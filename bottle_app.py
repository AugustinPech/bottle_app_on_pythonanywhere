# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template, error, static_file
import os
import caculator

@route('/')
def hello_world():
    return static_file('index.html', root='./views')

application = default_app()

if __name__ == "__main__":
    run()