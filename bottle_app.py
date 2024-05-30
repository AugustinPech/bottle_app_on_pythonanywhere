# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template, error, static_file
import os
import caculator
views_dir = os.path.join(os.path.dirname(__file__), 'views')
@route('/')
def hello_world():
    return static_file('index.html', root=views_dir)

application = default_app()

if __name__ == "__main__":
    run()

