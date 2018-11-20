from bottle import run, route, request


@route('/querytest')
def querytest():
    param1 = request.query.param1
    param2 = request.query.param2
    return '''
    the value of param1: {} \n
    the value of param2: {}
    '''.format(param1, param2)






if __name__ == '__main__':
    run(debug=True, reloader=True)


