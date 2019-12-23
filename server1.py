from flask import Flask, jsonify, request
from flask import abort, redirect, url_for, request
from zproductsDAO import productDAO

#create app
app = Flask(__name__, static_url_path='', static_folder='.')


# products = [
#     { "id":1, "Name": "Yog Nog", "Type": "Shower Gel", "Size": 250, "Price": 2000},
#     { "id":2, "Name": "Snow Fairy", "Type": "Shower Gel", "Size": 250, "Price": 2000},
#     { "id":3, "Name": "Yog Nog", "Type": "Body Conditioner", "Size": 125, "Price": 1500}
# ]

nextId = 4

#interface & functions

#curl http://127.0.0.1:5000/products
@app.route('/products')
def getAll():
    results = productDAO.getAll()
    return jsonify(results)

#curl http://127.0.0.1:5000/products/2
@app.route('/products/<int:id>')
def findById(id):
    #foundProduct = list(filter(lambda b: b['id'] == id, products))
    foundProduct = productDAO.findByID(id)
    # if len(foundProduct) == 0:
    #     return jsonify({}), 204
    return jsonify(foundProduct)

@app.route('/products', methods=['POST'])
def create():
    #global nextId
    if not request.json:
        abort(400)
    #check that request is properly formatted
    product = {
        #"id": nextId,
        "Name": request.json['Name'],
        "Type": request.json['Type'],
        "Size": request.json['Size'],
        "Price": request.json['Price']
    }
    # nextId += 1 #ensure counter stays correct
    # products.append(product)
    values =(product['Name'],product['Type'],product['Size'], product['Price'])
    newId = productDAO.create(values)
    product['id'] = newId
    return jsonify(product)

@app.route('/products/<int:id>', methods=['PUT'])
def update(id):
    foundProduct = productDAO.findByID(id)
    if not foundProduct:
        abort(400)
    # if len(foundProducts) == 0:
    #     return jsonify({}), 204
    # foundProduct = foundProducts[0]
    # if not request.json:
    #     abort(400)

    reqJson = request.json

    #verify input format
    if 'Size' in reqJson and type(reqJson['Size']) is not int:
        abort(400)
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    #update
    if 'Name' in reqJson:
        foundProduct['Name'] = reqJson['Name']
    if 'Type' in reqJson:
        foundProduct['Type'] = reqJson['Type']
    if 'Size' in reqJson:
        foundProduct['Size'] = reqJson['Size']    
    if  'Price' in reqJson:
        foundProduct['Price'] = reqJson['Price'] 

    values = (foundProduct['Name'],foundProduct['Type'],foundProduct['Size'], foundProduct['Price'], foundProduct['id'])
    productDAO.update(values)
    return jsonify(foundProduct)

@app.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    # foundProducts = list(filter(lambda b: b['id'] == id, products))
    # if len(foundProducts) == 0:
    #     return jsonify({}), 204
    # products.remove(foundProducts[0])
    productDAO.delete(id)
    return jsonify({"done":True})


#run flask
if __name__== '__main__':
    app.run(debug = True)