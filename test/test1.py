import unittest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import requests
import io
import sys

# Assuming the original script is named 'actor_info.py' and the function is 'main'
from script1 import main

class TestActorInfoExtraction(unittest.TestCase):

    @patch('requests.get')
    def test_actor_info_extraction(self, mock_get):
        # Sample HTML content based on the structure expected by the script
        sample_html = '''
        <html>
            <body>
                <h2 class="elementor-heading-title elementor-size-default">Emil Raste Karlsen</h2>
                <div class="elementor-element elementor-element-ec3227d elementor-widget elementor-widget-text-editor">
                    <p>Age: 30</p>
                    <p>Height: 180 cm</p>
                    <p>Nationality: Norwegian</p>
                </div>
            </body>
        </html>
        '''
        
        # Mocking the requests.get to return a response with the sample HTML content
        mock_response = Mock()
        mock_response.content = sample_html
        mock_get.return_value = mock_response
        
        # Redirecting stdout to capture the print output of the main function
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the main function
        main()
        
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Expected dictionary based on the sample HTML content
        expected_output = "{'name': 'Emil Raste Karlsen', 'age': '30', 'height': '180 cm', 'nationality': 'Norwegian'}\n"
        
        # Get the actual printed output
        actual_output = captured_output.getvalue()

        # Asserting the printed output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
