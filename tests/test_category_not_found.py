import unittest
from ..app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_category_not_found(self):
        invalid_category_id = 99999
        response = self.app.get(f'/api/videos/{invalid_category_id}')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data, {"error": "Category not found"})

if __name__ == '__main__':
    unittest.main()
