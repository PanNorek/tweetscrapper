import unittest
from src.AuthorizationManager import *

class TestAuthorizationManager(unittest.TestCase):

    instance = AuthorizationManager(r'E:/coding/pythonnew/tweetscrapper/your_api_keys_sample.json')

    def test_get_access_token(self):
        
        self.instance.get_access_token()
        self.assertEqual(self.instance.access_token, 'verylongstringhere')

    def test_get_access_token_secret(self):
            
            self.instance.get_access_token_secret()
            self.assertEqual(self.instance.access_token_secret, 'verylongstringhere')
    

    def test_get_bearer_token(self):
            
            self.instance.get_bearer_token()
            self.assertEqual(self.instance.bearer_token, 'veryverylongstringhere')
    
    def test_get_api_key(self):

        self.instance.get_api_key()
        self.assertEqual(self.instance.api_key,'longstringhere')
    
    def test_get_api_secret(self):
                
        self.instance.get_api_secret()
        self.assertEqual(self.instance.api_secret,'verylongstringhere')