import json

class AuthorizationManager:
    '''Simple class to get the keys  from a json file'''
    stored_keys_filename:str
    bearer_token:str
    api_key:str
    api_secret:str
    access_token:str
    access_token_secret:str
    app_id:str
    
    def __init__(self,stored_keys_filename:str):
        self.stored_keys_filename = stored_keys_filename
        with open('../'+stored_keys_filename,'r') as file:
            keys = json.load(file)
            self.bearer_token = keys['Bearer_Token']
            self.api_key = keys['API_Key']
            self.api_secret = keys['API_Key_Secret']
            self.access_token = keys['Access_Token']
            self.access_token_secret = keys['Access_Token_Secret']
            self.app_id = keys['App_ID']
    


    def get_bearer_token(self):
        return self.bearer_token

    def get_bearer_header(self):
        return {'Authorization': 'Bearer ' + self.bearer_token}
        
    def get_api_key(self):
        return self.api_key
    
    def get_api_secret(self):
        return self.api_secret
    
    def get_access_token(self):
        return self.access_token
    
    def get_access_token_secret(self):
        return self.access_token_secret
    
    def get_app_id(self):
        return self.app_id
    
    def get_keys(self):
        return {'Bearer_Token':self.bearer_token,
                'API_Key':self.api_key,
                'API_Secret':self.api_secret,
                'Access_Token':self.access_token,
                'Access_Token_Secret':self.access_token_secret,
                'App_ID':self.app_id}