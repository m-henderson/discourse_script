import unittest
import openai
from writefull import generate_title

class TestGenerateTitle(unittest.TestCase):
    
    def setUp(self):
        openai.api_key = "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"
        
    def test_generate_title(self):
        # Test with a short input
        input_text = "This is a short test post."
        expected_output = "Short Test Post"
        self.assertEqual(generate_title(input_text), expected_output)
        
        # Test with a longer input
        input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a arcu sed ex ultricies semper. Nulla facilisi. Sed gravida massa nisl, ut pellentesque justo auctor ut. In consectetur risus eget tortor vestibulum, vel gravida est hendrerit. Etiam imperdiet ligula auctor, elementum lectus eget, pellentesque massa. Aliquam ac bibendum est, nec imperdiet mauris. Nulla facilisi. Donec quis elit hendrerit, ullamcorper nulla in, tristique ipsum. Nam sit amet libero id magna aliquam consectetur."
        expected_output = "Lorem Ipsum Dolor Sit Amet"
        self.assertEqual(generate_title(input_text), expected_output)
        
if __name__ == '__main__':
    unittest.main()
