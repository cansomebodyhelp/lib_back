import unittest
from ..app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_categories(self):
        response = self.app.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('id', data[0])
        self.assertIn('name', data[0])
        self.assertIn('preview_link', data[0])

if __name__ == '__main__':
    unittest.main()
