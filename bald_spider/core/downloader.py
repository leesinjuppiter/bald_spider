import asyncio
import requests
import time

class Downloader:
    def __init__(self):
        pass

    async def download(self, url):
        # response = requests.get(url)
        # print(response)
        await asyncio.sleep(0.4)
        print('result')
