import os

from decouple import config
from imgurpython import ImgurClient

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
access_token = config('ACCESS_TOKEN')
refresh_token = config('REFRESH_TOKEN')
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
album = config('ALUBM_ID')


def upload_image(path):
    conf = {
        'album': album,
    }
    try:
        client.upload_from_path(path, config=conf, anon=False)
        os.remove(path)
    except:
        pass


def get_photos():
    img = client.get_album_images(album)
    return img
