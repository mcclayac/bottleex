from bottle import run, route


@route('/')
def index ():
    return '<h1>Hello, BigMan Bottle</h1>'

@route('/bigman')
def index ():
    return '<h1>Hello, BigMan Bottle - These Nutz</h1>'

if __name__ == '__main__':
    run()

