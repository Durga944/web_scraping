import urllib3
import requests
from pprint import pprint

http = urllib3.PoolManager()
r = http.request('GET', "https://www.imdb.com/title/tt0048473/mediaviewer/rm2023787521")
page = (r.data, "html.parser")
pprint(page)


