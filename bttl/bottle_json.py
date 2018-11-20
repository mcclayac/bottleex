from bottle import run, route




@route('/')
def index():
    return {'name' : 'json data', 'myList':[1,2,3,4,5,'apples','oranges','pears']}

    # return "<html><h1>  HTML    </h1></html>"






if __name__ == '__main__':
    run(debug=True, reloader=True)


