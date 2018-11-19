from bottle import run, route





@route('/login')
def login():
    return '<h1>Hello, BigMan Bottle - on the login page</h1>'


@route('/register')
def register():
    return '<h1>On the register Page</h1>'

@route('/article/<id>')
def articke(id):
    if id:
        return '<h1>You are viewing article {} </h1>'.format(id)
    else:
        return '<h1>No Article ID Present</h1>'

@route('/page/<id>/<name>')
def page(id, name):
    return 'you are viewing page id:{} and name:{}'.format(id, name)

@route('/posted', method='POST')
def posted():
    return 'This data is posted'


if __name__ == '__main__':
    run(debug=True, reloader=True)


