import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL_EQUIPMENT = "http://localhost:5000/api/equipment/"
    BASE_URL_REPAIR_REQUESTS = "http://localhost:5000/api/repair_requests/"

    def test_list_equipment(self):
        response = requests.get(self.BASE_URL_EQUIPMENT)
        self.assertEqual(response.status_code, 200)

    def test_add_equipment(self):
        new_equipment = {
            "name": "Тестовое оборудование",
            "type": "Тип 1",
            "location": "Место 1",
            "installation_date": "2023-01-01"
        }
        response = requests.post(self.BASE_URL_EQUIPMENT, json=new_equipment)
        self.assertEqual(response.status_code, 201)

    def test_list_repair_requests(self):
        response = requests.get(self.BASE_URL_REPAIR_REQUESTS)
        self.assertEqual(response.status_code, 200)

    def test_add_repair_request(self):
        new_request = {
            "equipment_id": 1,
            "description": "Не работает"
        }
        response = requests.post(self.BASE_URL_REPAIR_REQUESTS, json=new_request)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

