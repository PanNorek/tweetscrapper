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
    
    def __init__(self,stored_keys_filename:str)->None:
        self.stored_keys_filename = stored_keys_filename
        try:
            with open('../'+stored_keys_filename,'r') as file:
                keys = json.load(file)
                self.bearer_token = keys['Bearer_Token']
                self.api_key = keys['API_Key']
                self.api_secret = keys['API_Key_Secret']
                self.access_token = keys['Access_Token']
                self.access_token_secret = keys['Access_Token_Secret']
                self.app_id = keys['App_ID']
        except:
            with open(stored_keys_filename,'r') as file:
                keys = json.load(file)
                self.bearer_token = keys['Bearer_Token']
                self.api_key = keys['API_Key']
                self.api_secret = keys['API_Key_Secret']
                self.access_token = keys['Access_Token']
                self.access_token_secret = keys['Access_Token_Secret']
                self.app_id = keys['App_ID']


    def get_bearer_token(self) -> str:
        """
        Getter for bearer_token
    
            Returns:
         (str): Twitter API bearer token.
        """
        return self.bearer_token

    def get_bearer_header(self)-> str:
        """
        Getter for bearer_token
    
            Returns:
         (str): Twitter API bearer token.
        """
        return {'Authorization': 'Bearer ' + self.bearer_token}
        
    def get_api_key(self)-> str:
        """
        Getter for api_key
    
            Returns:
        preprocessedText (str): Twitter API api_key.
        """
        return self.api_key
    
    def get_api_secret(self)-> str:
        """
        Getter for api_secret
    
            Returns:
         (str): Twitter API api_secret.
        """
        return self.api_secret
    
    def get_access_token(self)-> str:
        """
        Getter for access_token
    
            Returns:
         (str): Twitter API access_token.
        """
        return self.access_token
    
    def get_access_token_secret(self)-> str:
        """
        Getter for bearer_token
    
            Returns:
         (str): Twitter API access_token_secret.
        """
        return self.access_token_secret
    
    def get_app_id(self)-> str:
        """
        Getter for app_id
    
            Returns:
         (str): Twitter API app_id.
        """
        return self.app_id
    
    def get_keys(self)-> dict:
        """
        Getter for all Twitter Api keys
    
            Returns:
         (dict):  All keys you get on Twitter API.
        """
        return {'Bearer_Token':self.bearer_token,
                'API_Key':self.api_key,
                'API_Secret':self.api_secret,
                'Access_Token':self.access_token,
                'Access_Token_Secret':self.access_token_secret,
                'App_ID':self.app_id}