from bottle import run, route, template




@route('/')
def index ():
    return template('index', name='Tony')






if __name__ == '__main__':
    run(debug=True, reloader=True)







