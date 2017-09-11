# Typechecked Mock

Provides a mock object that requires all its arguments are called with the correct types.

# Usage:

lib.py

```python
import requests


def get_user_by_id(user_id: int):
    # dummy implementation
    return requests.get(f'https://httpbin.org/anything/{user_id}').json()
```

app.py

```python
from lib import get_user_by_id


def get_user_url(user_id: str):
    user_info = get_user_by_id(user_id)  # This is called with the wrong type
    return user_info['url']
```

test.py:

```python
from unittest import TestCase
from typed_mock import patch


MOCK_URL = 'http://example.com'


class TestApp(TestCase):

    @patch('lib.get_user_by_id', TypedMock(return_value={'url': MOCK_URL}))
    def test_get_user_url(self):
        url = get_user_url('9')

        self.assertEquals(url, MOCK_URL)
```

```
python -m unittest
FAIL you called get_user_url with '9' (type: str) however it expects type `int`.
```

# Why?

The above error could easily be caught by mypy without even having a test. So why create this library?

When working with large and/or legacy codebases, however, particularly ones that use a framework such as Django, I've found it to be impractical to typecheck an entire codebase - mypy runs too slowly and produces too much noise.

Additionally, when testing application code that integrates with an external api, mocks help allow for testing, but they often miss errors due to missing / incorrect arguments. [autospec](link) can help, but that still ignores type errors.


# Caveats

Only works on methods for now
