from azure.storage.blob import ContainerClient, BlobServiceClient
import json


def get_data_from_blob(
    module: str,
    account_key: str,
):
    account_name = "storagedatacademy"
    STORAGEACCOUNTURL = f"https://{account_name}.blob.core.windows.net"

    if 'm5' in module.lower():
        container_name = "m5-api"

    container = ContainerClient.from_connection_string(
        conn_str=f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net",
        container_name=container_name)

    blob_list = container.list_blobs()

    blob_service_client_instance = BlobServiceClient(
        account_url=STORAGEACCOUNTURL, credential=account_key)

    results = {}

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
