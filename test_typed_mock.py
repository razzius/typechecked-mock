from unittest import TestCase
from unittest.mock import Mock

from typed_mock import patch, MockTypeError

from app import get_user_url


MOCK_URL = 'http://example.com'


class TestApp(TestCase):

    @patch('app.get_user_by_id', Mock(return_value={'url': MOCK_URL}))
    def test_get_user_url_by_kwarg(self):
        with self.assertRaises(MockTypeError):
            get_user_url(user_id='9')

    @patch('app.get_user_by_id', Mock(return_value={'url': MOCK_URL}))
    def test_get_user_url_by_arg(self):
        with self.assertRaises(MockTypeError):
            get_user_url('9')

    def test_cannot_autospec(self):
        with self.assertRaises(ValueError):
            patch('app.get_user_by_id', autospec=True)

    @patch('app.get_user_by_id', Mock(return_value={'url': MOCK_URL}))
    def test_passing_no_arguments_fails(self):
        with self.assertRaises(TypeError):
            get_user_url()
