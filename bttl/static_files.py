from bottle import run, route, static_file, template




@route('/')
def index ():
    return template('index2')


@route('/staticf/<filename>')
def staticf(filename):
    l_fileName = filename
    print('In Method staticf')
    return(static_file(filename, root='./static_images'))



if __name__ == '__main__':
    run(debug=True, reloader=True)


