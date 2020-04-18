import requests, json
from urllib.parse import quote

class AuthenticationFailure(Exception):
    pass

class BadJSON(Exception):
    pass

class BadRawValue(Exception):
    pass

class S1:
    def __init__(self, token):
        self.base_url = 'https://s1.kognise.dev'
        self.token = token
    
    def set(self, key, value):
        try:
            value = bytes(json.dumps(value).encode('utf-8'))
            response = requests.put(self.base_url + '/db/' + quote(key), data=value, headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8', 'Content-Length': str(len(value))})
            if not response.ok:
                raise requests.HTTPError("HTTP Error: " + response.text)
        except:
            raise BadJSON("Error parsing JSON for Key: " + key + ", did you mean to use set_raw?")
    
    def get(self, key):
        response = requests.get(self.base_url + '/db/' + quote(key), headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8'})
        if not response.ok:
            raise requests.HTTPError("HTTP Error: " + response.text)
        else:
            try:
                return json.loads(response.content)
            except json.JSONDecodeError:
                raise BadJSON("Error parsing JSON for Key: " + key + ", did you mean to use get_raw?")
            
    def set_raw(self, key, value):
        if type(value) != str:
            raise BadRawValue("Value:", value, "is not a valid string, did you mean to use set_raw?")
        else:
            value = bytes(value.encode('utf-8'))
            response = requests.put(self.base_url + '/db/' + quote(key), data=value, headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8', 'Content-Length': str(len(value))})
            if not response.ok:
                raise requests.HTTPError("HTTP Error: " + response.text)
            
    def get_raw(self, key):
        response = requests.get(self.base_url + '/db/' + quote(key), headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8'})
        if not response.ok:
            raise requests.HTTPError("HTTP Error: " + response.text)
        else:
            try:
                return response.text
            except json.JSONDecodeError:
                raise BadJSON("Error parsing JSON for Key: " + key + ", did you mean to use get_raw?")
                
    
    def get_keys(self):
        response = requests.get(self.base_url + '/db/', headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8'})
        if not response.ok:
            raise requests.HTTPError("HTTP Error: " + response.text)
        else:
            return response.json()
        
    def delete(self, key):
        response = requests.delete(self.base_url + '/db/' + key, headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'text/plain;charset=UTF-8'})
        if not response.ok:
            raise requests.HTTPError("HTTP Error: " + response.text)
