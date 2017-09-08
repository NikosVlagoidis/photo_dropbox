import os

from decouple import config
from imgurpython import ImgurClient

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
access_token = config('ACCESS_TOKEN')
refresh_token = config('REFRESH_TOKEN')


def upload_image(path):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    conf = {
        'album': 'Tjzcc',
    }
    res = client.upload_from_path(path, config=conf, anon=False)
    os.remove(path)
    return res
