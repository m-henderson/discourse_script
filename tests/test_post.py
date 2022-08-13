import json
import unittest
from post import should_process
from tests.utils.posts import short_body_post, long_body_post, dirty_body_post, clean_body_post
from utils.tools import clean_text_body


class TestPostMethods(unittest.TestCase):
    def test_should_process(self):
        self.assertTrue(should_process(long_body_post()))
        self.assertFalse(should_process(short_body_post()))

    def test_clean_post_body(self):
        self.assertEqual(clean_text_body(dirty_body_post()), clean_body_post())

if __name__ == "__main__":
    unittest.main()