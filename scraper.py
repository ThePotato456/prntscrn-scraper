from random import randrange
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import shutil
import sys
from io import BytesIO
import string
import time
import random
import os

def generate_link():
    source = string.ascii_letters + string.digits
    result_str = (''.join((random.choice(source) for i in range(6)))).lower()
    return (result_str)

if len(os.listdir('images/')):
    file_count = (len(os.listdir('images/')))
else:
    file_count = 0

try_count = 0
while True:
    try_count = try_count + 1
    url = "https://prnt.sc/" + generate_link()
    sys.stdout.write('\r[{}] Trying {}'.format(try_count, url))
    parser = 'html.parser' 
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"})
    http_encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(response.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(response.content, parser, from_encoding=encoding)
    
    time.sleep(0.01)
    for image in soup.find_all('img', src=True):
        if 'https://image.prntscr.com/image/' in image['src']:
            file_count = file_count + 1
            print(' -> Image link for {}: {} ({})'.format(url[(len("https://prnt.sc/")):], image['src'], file_count))
            file_name = os.path.join('images',image['src'][32:])
            if os.path.exists(file_name):
                break
            dl = requests.get(image['src'], stream=True, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"})
            with open(file_name, "wb") as image_file:
                shutil.copyfileobj(BytesIO(dl.content), image_file)
    sys.stdout.flush()

    time.sleep(0.3)