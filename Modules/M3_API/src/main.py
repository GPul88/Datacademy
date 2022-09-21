import json
import os
from fastapi import FastAPI

app = FastAPI()

with open(f"{os.getcwd().split('Datacademy')[0]}Datacademy\data\M3_API\customers.json", 'rb') as jsonFile:
    customers = json.load(jsonFile)
    customers = {i: customers[str(i)] for i in range(len(customers.keys()))}

@app.get("/get-customer/{customerId}")
def get_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists yet."}
    return customers[customerId]

# @app.get("/get-customer-by-name/")
# def get_customer_by_name(lastName: str):
#     for customerId in customers:
#         if customers[customerId]['lastName'] == lastName:
#             return customers[customerId]
    
#     return {"Error", f"Customer with last name: '{lastName}' does not exists"}

# @app.get("/get-customers/")
# def get_customers(skip: int, limit: int):
#     return {i: customers[i] for i in range(skip, min(skip+limit, len(customers)))}

@app.post("/create-customer/{customerId}")
def create_customer(customerId: int, firstName: str, lastName: str, address: str):
    if customerId in customers:
        return {"Error", f"customerId already used, next id available is: {max(customers.keys())+1}."}
    
    customers[customerId] = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address
    }
    return customers[customerId]

@app.put("/update-customer-address/{customerId}")
def update_customer_address(customerId: int, address: str):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}
    
    customers[customerId]['address'] = address
    return customers[customerId]

@app.delete("/delete-customer/{customerId}")
def delete_customer(customerId:int):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}
    
    del customers[customerId]
    return {"Message": " Student deleted successfully."}