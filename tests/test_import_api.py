import pytest
from api.import_api import ImportAPI
from utils.data_generator import generate_person_ids
from db.persons_table import PersonsTable

class TestImportAPI:

    @classmethod
    def setup_class(cls):
        cls.import_api = ImportAPI()
        cls.persons_table = PersonsTable()

    @pytest.mark.parametrize("person_id", generate_person_ids(3))
    def test_import_person_happy_path(self, person_id):
        response = self.import_api.import_person(person_id)
        assert response is not None
        assert response.status_code == 200

        # Validamos contra la bd
        expected = self.persons_table.get_person(person_id)
        assert expected is not None, f"personId {person_id} no encontrado en DynamoDB"
        assert expected["personId"] == person_id
        print(f"Happy path OK - personId: {person_id}, Response: {response.json()}")

    def test_import_person_invalid(self):
        person_id = None  # personId ausente
        response = self.import_api.import_person(person_id)
        assert response.status_code == 400
        body = response.json()
        assert body.get("message") == "Bad Request"
        assert body.get("cause") == "Incorrect user"
        print(f"Invalid ID - Response: {response.text}")

    def test_import_person_without_token(self):
        person_id = 111  # Id valido
        response = self.import_api.import_person_without_token(person_id)
        assert response.status_code == 401
        body = response.json()
        assert body.get("message") == "Unauthorized"
        print(f"No token - Response: {response.text}")

    def test_import_person_with_expired_token(self):
        person_id = 111  # Id valido
        response = self.import_api.import_person_without_token(person_id)
        assert response.status_code == 403
        body = response.json()
        assert body.get("message") == "User is not authorized to access this resource with an explicit deny"
        print(f"Expired token - Response: {response.text}")

