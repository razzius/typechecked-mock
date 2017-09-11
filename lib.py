import requests


def get_user_by_id(user_id: int):
    # dummy implementation
    return requests.get(f'https://httpbin.org/anything/{user_id}').json()
