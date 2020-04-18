from s1db import S1, BadJSON, BadRawValue, AuthenticationFailure
from uuid import uuid4
import unittest, requests


token = requests.get('https://s1.kognise.dev/token').text
api = S1(token)
normal_key = "TestKey-" + str(uuid4()).split('-')[1]
raw_key = "TestKey-" + str(uuid4()).split('-')[1]

class TestS1API(unittest.TestCase):
    
    def test_1_configure(self):
        self.assertIsNotNone(token)
        self.assertIsNotNone(api)
        
    def test_2_set_object(self):
        value = {'foo': 'bar'}
        api.set(normal_key, value)
        
    def test_3_get_object(self):
        result = api.get(normal_key)
        self.assertTrue(type(result) == dict)
        self.assertIsNotNone(result)
    
    def test_4_get_raw_object(self):
        result = api.get_raw(normal_key)
        self.assertTrue(type(result) == str)
        self.assertIsNotNone(result)
    
    def test_5_set_raw_object(self):
        api.set_raw(raw_key, '{"testing"}')

    def test_6_get_raw_object(self):
        result = api.get_raw(raw_key)
        self.assertTrue(type(result) == str)
    
    def test_7_get_raw_with_get(self):
        self.assertRaises(BadJSON, api.get, raw_key)
        
    def test_8_set_object_in_raw(self):
        self.assertRaises(BadRawValue, api.set_raw, normal_key + '0', {'foo': 'bar'})
        
    def test_9_get_all_keys(self):
        result = api.get_keys()
        self.assertTrue(type(result) == list)
        self.assertTrue(len(result) > 0)
        
    def test_a1_delete_key(self):
        api.delete(raw_key)
    
    def test_a2_authentication_handler(self):
        api2 = S1('badtoken')
        self.assertRaises(requests.HTTPError, api2.get, 'test')