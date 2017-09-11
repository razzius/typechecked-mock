from lib import get_user_by_id


def get_user_url(*args, **kwargs):
    user_info = get_user_by_id(*args, **kwargs)
    return user_info['url']
