import unittest
import jvpm.HelloWorld  # changed to absolute import, error has been fixed
from unittest.mock import patch, call

class TestHelloWorld(unittest.TestCase):
    @patch('builtins.print')
    def test_HelloWorld(self, mock_print):
        jvpm.HelloWorld.HelloWorld()
        self.assertEqual(mock_print.mock_calls, [
            call('Hello World'),
            call('Hello Robb'),
            call('Hello Megan'),
            call('Hello Justin'),
            call('Hello John'),
            call('Hello Josh'),
            call('Hello Calan'),
            call('Hello Riverz')
        ])
