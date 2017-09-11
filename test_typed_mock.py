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

    # TODO Uncomment. autospect does not work yet
    # @patch('app.get_user_by_id', autospec=True)
    # def test_get_user_url_missing_arg(self):
    #     url = get_user_url()

    #     self.assertEquals(url, MOCK_URL)
