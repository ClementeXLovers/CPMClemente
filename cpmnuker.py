import requests
import json
from time import sleep

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

BASE_URL: str = "https://cpmnuker.anasov.ly/api"

class CPMNuker:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = json.loads(response.text)
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        # response = requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)
        # response_decoded = json.loads(response.text)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = json.loads(response.text)
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_coins", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_name", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_id", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_plates", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/delete_friends", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_w16", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_horns", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/disable_damage", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlimited_fuel", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_race_wins", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_race_loses", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_houses", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    