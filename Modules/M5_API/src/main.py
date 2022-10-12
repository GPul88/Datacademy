from fastapi import FastAPI
from pydantic import BaseModel
from get_data import get_data_from_blob
import os
from dotenv import load_dotenv


load_dotenv()

account_key = os.getenv("AZURE_ACCOUNT_KEY")

data = get_data_from_blob(
    module="M5",
    account_key=account_key)
customers = data['customers.json']


app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome at the Module 5 API!"


# create customer Classes
class Customer(BaseModel):
    firstName: str
    lastName: str
    address: str


class CustomerAddress(BaseModel):
    address: str


class CustomerName(BaseModel):
    firstName: str
    lastName: str


# API GET Request(s) ####
@app.get("/get-customer/{customerId}")
def get_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists yet."}
    return customers[customerId]


@app.get("/get-customer-by-name/{lastName}")
def get_customer_by_name(lastName: str):
    for customerId in customers:
        if customers[customerId]['lastName'] == lastName:
            return customers[customerId]

    return {"Error", f"Customer with last name: '{lastName}' does not exists"}


@app.get("/get-customers/")
def get_customers(skip: int = 0, limit: int = 3):
    return {i: customers[i] for i in range(skip, min(skip+limit, len(customers)))}


# API POST Request(s) ####
@app.post("/create-customer/{customerId}")
def create_customer(customerId: int, customer: Customer):
    if customerId in customers:
        return {"Error", f"customerId already used, next id available is: {max(customers.keys())+1}."}

    customers[customerId] = {
        "firstName": customer.firstName,
        "lastName": customer.lastName,
        "address": customer.address
    }
    return customers[customerId]


@app.post("/create-customer-auto-increment/")
def create_customer_autoincrement(customer: Customer):
    customerId = max(customers.keys()) + 1

    customers[customerId] = {
        "firstName": customer.firstName,
        "lastName": customer.lastName,
        "address": customer.address
    }
    return customers[customerId]


# API PUT Request(s) ####
@app.put("/update-customer-address/{customerId}")
def update_customer_address(customerId: int, customer_address: CustomerAddress):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    customers[customerId]['address'] = customer_address.address
    return customers[customerId]


@app.put("/update-customer-address-by-name/")
def update_customer_address_by_name(customer: Customer):
    for customerId in customers:
        if customers[customerId]['firstName'] == customer.firstName and customers[customerId]['lastName'] == customer.lastName:
            customers[customerId]['address'] = customer.address

            return customers[customerId]


# API DELETE Request(s) ####
@app.delete("/delete-customer/{customerId}")
def delete_customer(customerId: int):
    if customerId not in customers:
        return {"Error", "Customer does not exists."}

    del customers[customerId]
    return {"Message": f"Customer {customerId} deleted successfully."}


@app.delete("/delete-customer-by-name/")
def delete_customer_by_name(name: CustomerName):
    foundCustomer = False
    for customer in customers:
        if customers[customer]['firstName'] == name.firstName and customers[customer]['lastName'] == name.lastName:
            foundCustomer = True
            del customers[customer]
            break

    if not foundCustomer:
        return {"Error": "The customer you are trying to delete does not exist."}
    else:
        return {"Message": f"Customer {name.firstName} {name.lastName} deleted successfully."}
