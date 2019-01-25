import requests

from django.conf import settings
from django.db.models import Count

from django.core.cache import cache

# get the cache key for storage
def cache_get_key(*args, **kwargs):
    import hashlib
    serialise = []
    for arg in args:
        serialise.append(str(arg))
    for key, arg in kwargs.items():
        serialise.append(str(key))
        serialise.append(str(arg))
    key = hashlib.md5("".join(serialise)).hexdigest()
    return key

# decorator for caching functions
def cache_for(time):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            key = cache_get_key(fn.__name__, *args, **kwargs)
            result = cache.get(key)
            if not result:
                result = fn(*args, **kwargs)
                cache.set(key, result, time)
            return result
        return wrapper
    return decorator


# 1 hour
cacheTime = 60 * 60


@cache_for(cacheTime)
def get_feed():
    print('---------')
    print('HIT CACHE')
    print('---------')

    # assemble variables before request
    url = 'https://www.instagram.com/cranble/'
    url_split = url.split('/')
    # - 2 to ignore the blank string at the end, and also to account for list index starting at 0
    account = url_split[(len(url_split) - 2)]

    # send request
    r = requests.get(url)

    # assign images to array
    images_split = r.text.split('eight":480},{"src":"')
    images = []
    for i in images_split[1:]:
        images.append(i.split('"')[0])

    # set variables from request data
    info = r.text.split('<meta content="')[1].split('Posts -')[0]
    info_split = (info + 'Posts').split(', ')
    followers = info_split[0]
    following = info_split[1]
    posts = info_split[2]
    avatar_image = r.text.split('"profile_pic_url":"')[1].split('"')[0]
    return {
        'account': account,
        'url': url,
        'feed': images,
        'followers': {
            'number': followers.split(' ')[0],
            'unit': followers.split(' ')[1],
        },
        'following': {
            'number': following.split(' ')[0],
            'unit': following.split(' ')[1],
        },
        'posts': {
            'number': posts.split(' ')[0],
            'unit': posts.split(' ')[1],
        },
        'avatar_image': avatar_image,
    }


def meta(self):
    return {
        'instagram_feed': get_feed()
    }

