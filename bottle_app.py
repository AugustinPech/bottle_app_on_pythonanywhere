
# A very simple Bottle Hello World app for you to get started with...

from bottle import default_app, route, run, template, error, static_file


abs_views_path= os.path.join(os.getcwd(), 'views')

@route('/')
def hello_world():
    return static_file('index.html', root=abs_views_path)

application = default_app()