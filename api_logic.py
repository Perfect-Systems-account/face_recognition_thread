import requests
from requests.auth import HTTPDigestAuth


# TO1DO - get the camera data from the SQL

def intercom_open_door(ip,username,password): #port
    print('in open door')
    url = f"http://{ip}/ISAPI/AccessControl/RemoteControl/door/65535"
    xml_payload = """
    <RemoteControlDoor version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
      <cmd>open</cmd>
    </RemoteControlDoor>
    """

    headers = {
        'Content-Type': 'application/xml',
    }

    auth = HTTPDigestAuth(username, password)
    response = requests.put(url, data=xml_payload, headers=headers, auth=auth)

    # Check the response
    if response.status_code == 200:
        print("Request successful status code:")
    else:
        print("Request failed with status code:")
        print(response.text)
