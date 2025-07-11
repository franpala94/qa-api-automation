import requests
import os
from dotenv import load_dotenv

# Llama las variables que tenemos en el .env
load_dotenv()

class ImportAPI:

    def __init__(self):
        # Seteamos las urls
        self._base_url = "https://api.test.worldsys.ar"
        self._import_url = f"{self._base_url}/import"

    @staticmethod
    def headers_content_type_json(token_type='valid'):
        """
        This method return a headers, adding a valid token with the data obtained.
        :return: headers json
        """
        # Llamamos el valor de token del .env
        if token_type == 'valid':
            token = os.getenv("API_TOKEN")
            if not token:
                raise ValueError("API_TOKEN no está definido en el .env")
        else:
            token = os.getenv("EXPIRED_TOKEN")
            if not token:
                raise ValueError("EXPIRED_TOKEN no está definido en el .env")

        # Retornamos el header completo
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def import_person(self, person_id):
        # Seteamos el body
        payload = [{"personId": person_id}]

        # Le pegamos a la api
        try:
            response = requests.post(self._import_url, json=payload, headers=self.headers_content_type_json())
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST request: {e}")
            return None

    def import_person_without_token(self, person_id):
        # Seteamos el body
        payload = [{"personId": person_id}]
        # Seteamos el header sin el token
        headers = {
            "Content-Type": "application/json",
            "Authorization": ""
        }
        # Le pegamos a la api
        try:
            response = requests.post(self._import_url, json=payload, headers=headers)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST request: {e}")
            return None

    def import_person_with_expired_token(self, person_id):
        # Seteamos el body
        payload = [{"personId": person_id}]

        # Le pegamos a la api
        try:
            response = requests.post(self._import_url, json=payload, headers=self.headers_content_type_json(token_type='invalid'))
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST request: {e}")
            return None

