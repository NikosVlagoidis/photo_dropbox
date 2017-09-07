import os

from decouple import config
from imgurpython import ImgurClient

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static')

path = os.path.join(UPLOAD_FOLDER, 'download.jpg')

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
access_token = config('ACCESS_TOKEN')
refresh_token = config('REFRESH_TOKEN')

client = ImgurClient(client_id, client_secret, access_token, refresh_token)

res = client.upload_from_path(path, config=None, anon=False)
print(res)
