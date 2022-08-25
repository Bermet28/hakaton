import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

id_ = 7
def get_id():
    global id_
    id_ += 1
    return id_

def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'brand': input('brand: '),
        'model': input('model of product: '),
        'year': input('year: ' ),
        'price': float(input('price: ')),
        'description': input('enter description:')}
    data.append(product)
    json.dump(data, open(FILE_PATH, 'w'))
    
    return 'Created!'


def list_of_products():
    data = get_data()
    for product in data: 
        print(f'{product}')
    return 'list'


def detail_retrieve():
    data = get_data()
    id_ = int(input('Enter id of product: '))
    product = list(filter(lambda x: x['id'] == id_, data))
    for i in product:
        print(f'{i}\n')
    return 'model'

def update_product():
    data = get_data()
    id_ = int(input('Enter id of product: '))
 
    product = list(filter(lambda x : x['id'] == id_, data))[0]
    index = data.index(product)

    if not product: return 'NOT FOUND'
    choice = input('Cho izmenit\'?\n1 -brand, 2 - model, 3 - price, 4 -descrpintion, 5 -year   ')

    if choice == '1':
        data[index]['brand'] = input('Enter new brand: ')

    elif choice == '2':

        data[index]['model'] = input('Enter new model: ')

    elif choice == '3':
        data[index]['price'] = input('Enter new price: ')
    
    elif choice == '4':
        data[index]['description'] = input('Enter new discsription: ')

    elif choice == '5':
        data[index]['year'] = input('Enter new year: ')

    else:
        return('Nekkorrecrnyu vybor')

    json.dump(data, open(FILE_PATH, 'w'))
    return('Succesfully updated')

def delete_product():
    data = get_data()
    id_product = int(input('Enter id of product: '))
  
    product = list(filter(lambda x : x['id'] == id_product, data))[0]
    if not product: return 'NOT FOUND'

    index = data.index(product)
    data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))
    return 'Succesfully deleted'


