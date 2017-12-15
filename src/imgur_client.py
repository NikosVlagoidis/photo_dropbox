import os

from celery import Celery
from decouple import config
from imgurpython import ImgurClient

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
access_token = config('ACCESS_TOKEN')
refresh_token = config('REFRESH_TOKEN')
broker = config('CELERY_BROKER_URL')
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
album = config('ALBUM_ID')
celery = Celery('tasks', broker=broker)


@celery.task
def upload_image(path):
    conf = {
        'album': album,
    }
    try:
        client.upload_from_path(path, config=conf, anon=False)
        os.remove(path)
    except Exception as e:
        print(e)


def get_photos():
    img = client.get_album_images(album)
    return img
