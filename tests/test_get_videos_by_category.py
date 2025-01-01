import unittest
from ..app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_videos_by_category(self):
        category_id = 1
        response = self.app.get(f'/api/videos/{category_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        if len(data) > 0:
            self.assertIn('id', data[0])
            self.assertIn('name', data[0])
            self.assertIn('preview_link', data[0])
            self.assertIn('video_id', data[0])
            self.assertIn('category_name', data[0])
        else:
            self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()
