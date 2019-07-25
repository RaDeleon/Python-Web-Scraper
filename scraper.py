from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.youtube.com/results?search_query=python')

res.text


print(res.text)
















# TODO:
# * Count total number of views for all videos on 1st page of youtube for given keyword
# * Keyword = Python