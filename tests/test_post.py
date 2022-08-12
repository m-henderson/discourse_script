import json
import unittest
from post import should_process
from tests.utils.posts import short_body_post, long_body_post

class TestPostMethods(unittest.TestCase):
    def test_should_process(self):
        self.assertTrue(should_process(long_body_post()))
        self.assertFalse(should_process(short_body_post()))

if __name__ == "__main__":
    unittest.main()