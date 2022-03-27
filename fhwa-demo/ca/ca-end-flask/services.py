import requests

#get list of connections
def get_connections(URL,PARAMS):
    try:
        r = requests.get(url=URL,params=PARAMS)
        get_result = r.json()["results"]
        connection_dict = {}
        for connection in get_result:
            their_did = connection["their_did"]
            connection_id = connection["connection_id"]
            connection_dict[their_did] = connection_id
    except:
        connection_dict = {}
    return connection_dict


#get list of schemas created
def get_schemas(URL,PARAMS):
    try:
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()["schema_ids"]
    except:
        data = {}
    return data

#get created credential definitions
def get_credential_definitions(URL,PARAMS):
    try: 
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()["credential_definition_ids"]
    except:
        data = {}
    return data

#get DIDs of 

#get users Verkeys
def get_verkeys(URL,DID):
    r = requests.get(url=URL,params=DID)
    data = r.json()["verkey"]
    return data

#get json
def get_json(URL,json_object):
    r = requests.get(url=URL,json=json_object)
    data = r.json()
    return data

#handle post json
def handle_json(URL,json_object):
    r = requests.post(url=URL,json=json_object)
    data = r.json()
    return data