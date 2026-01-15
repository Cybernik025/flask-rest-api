from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            },
                        {
                "name": "Table",
                "price": 40.99
            }
        ]
    }
]
# tells flask this function should run when the client makes a HTTP GET request
# "/store" is the end point or URL path
@app.get("/stores") # http://127.0.0.1:5000/store
def get_stores():
# same as just return stores but it is done this way so that the JSON respose would also
# include "stores:" and the output instead of just the output. This is better for readability
    return {"stores": stores}

@app.post("/stores")
def create_store():
    # Receives the JSON string as a python dictionary
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    # returns what was added to the client along with 
    # status code 201 which means new data accepted and added
    return new_store, 201

# When the store name and item is sent in the request URL from the client
@app.post("/stores/<string:name>/item")
def create_item(name):
    request_data = request.get_json()

    for store in stores:
        if name == store["name"]:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "Store not found"}, 404
        
@app.get("/stores/<string:name>") 
def get_store(name):
    for store in stores:
        if name == store["name"]:
            return {"store": store} # flask will convert this to JSON
    
    return {"message": "Store not found"}, 404

@app.get("/stores/<string:name>/item") 
def get_item_in_store(name):
    for store in stores:
        if name == store["name"]:
            # could return just a list store["items"] instead
            # of a JSON object, but its better this way for clients
            return {"items": store["items"]}
    
    return {"message": "Item not found"}, 404
