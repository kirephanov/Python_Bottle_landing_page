from bottle import route, run, template, TEMPLATE_PATH, static_file

TEMPLATE_PATH.append("./templates")

# Routes
@route('/')
def index():
    return template('index.tpl')

# Static
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

if __name__ == "__main__":
    run(host='localhost', port=8080)