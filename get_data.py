from datetime import datetime
from azure.storage.blob import ContainerClient, BlobServiceClient
import json
import pandas as pd
from azure.core.exceptions import ResourceNotFoundError


def authenticate(datacademy_id: str):
    ids = pd.read_csv(
        "https://storagedatacademy.blob.core.windows.net/src/ids.csv?sv=2021-04-10&st=2022-10-12T09%3A14%3A34Z&"
        "se=2029-10-13T09%3A14%3A00Z&sr=b&sp=r&sig=LbbsK8LMBNsGL4soycKpnMyDq8iABypUTCNQS5f1CrQ%3D", sep=";")
    ids["valid_from"] = ids["valid_from"].map(lambda x: datetime.strptime(x, '%d-%m-%Y'))
    ids["valid_to"] = ids["valid_to"].map(lambda x: datetime.strptime(x, '%d-%m-%Y'))

    valid_id = ids.loc[
        (ids["id"] == datacademy_id) & (ids["valid_from"] <= datetime.now()) & (ids["valid_to"] >= datetime.now())]
    if len(valid_id) >= 1:
        return True
    else:
        return False


def get_data_from_blob(
    module: str,
    datacademy_id: str,
):
    # check if user is authenticated to get data
    assert authenticate(datacademy_id=datacademy_id), "Please make sure that you have a valid datacademy id"

    account_name = "storagedatacademy"
    account_key = "kBDGxqup8rx6oCTv81v9DGTmqeSdpply+hUd9fyzI46+ufMizhRG+YJGl48PVIh8PeueYMFtWLsD+AStzV8Qrg=="
    STORAGEACCOUNTURL = f"https://{account_name}.blob.core.windows.net"

    container_name = module.lower().replace("_", "-")

    container = ContainerClient.from_connection_string(
        conn_str=f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net",
        container_name=container_name)

    blob_list = container.list_blobs()

    blob_service_client_instance = BlobServiceClient(
        account_url=STORAGEACCOUNTURL, credential=account_key)

    results = {}
    try:
        for i, BLOBNAME in enumerate(blob_list):
            # make new folder if it doesn't exist yet
            if ".json" in BLOBNAME.name:
                blob_client_instance = blob_service_client_instance.get_blob_client(
                    container_name, BLOBNAME, snapshot=None)
                # download blob
                blob_data = blob_client_instance.download_blob()
                # read JSON as bytes
                tmp = json.loads(blob_data.readall().decode("utf-8"))
                # set key as integer
                results[BLOBNAME.name] = {int(k): tmp[v] for k, v in enumerate(tmp)}

            if ".csv" in BLOBNAME.name:
                # tell python what to do with file, i.e. pd.read_csv(...)
                pass
        return results
    except ResourceNotFoundError:
        print("Please provide a valid module name")
