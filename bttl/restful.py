from bottle import run, route, get, post, request, delete


animals = [{'name': 'Ellie',    'type':'Elephant'},
           {'name': 'Python',   'type':'Snake'},
           {'name': 'Zed',      'type':'Zebra'}]


@get('/animal')
def getAll():
    return {'animal':animals}


@get('/animal/<name>')
def getOne(name):
    the_Animal = [animal for animal in animals if animal['name'] ==name]
    return {'animal':the_Animal[0]}

@post('/animal')
def addOne():
    new_animaal = {'name': request.json.get('name'), 'type': request.json.get('type')}
    animals.append(new_animaal)
    return {'animal': animals}

@delete('/animal/<name>')
def deleteAnimal(name):

    the_Animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(the_Animal[0])

    return {'animal':animals}

    # if name in animals:
    #     aAnimal = animals[name]
    #     del(animals[name])
    #     # animals.remove()
    #     aAnimal['status':'deleted']
    #     return {'animal':aAnimal}
    # else:
    #     returnValue = {}
    #     returnValue['status':'NO Animal of that name']
    #     return {'animal': returnValue }

# @route('/')
# def index ():
#     return template('index', name='Tony')

if __name__ == '__main__':
    run(debug=True, reloader=True)







