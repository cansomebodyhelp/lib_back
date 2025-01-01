import unittest
from ..app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_video_response_format(self):
        category_id = 1
        response = self.app.get(f'/api/videos/{category_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        for video in data:
            self.assertIn('id', video)
            self.assertIn('name', video)
            self.assertIn('preview_link', video)
            self.assertIn('video_id', video)
            self.assertIn('category_name', video)
            self.assertIn('description', video)

if __name__ == '__main__':
    unittest.main()
