import random
import string
from requests_html import *

failed_url_list = []


def save_image(url_list: list):
    with ThreadPoolExecutor() as executor:
        [executor.submit(save_image_requests, url) for url in url_list]


def name_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def save_image_requests(src):
    try:
        r = requests.get(src)
        file_name = name_generator()
        with open(f'pic/{file_name}.jpg', 'wb') as outfile:
            outfile.write(r.content)
        print(f'{file_name} -> Downloaded {src}')
    except Exception as ex:
        failed_url_list.append(src)
        print(f'Error {ex} url:{src}')
