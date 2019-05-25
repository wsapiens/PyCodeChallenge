#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

def getMovieTitles(substr):
    titles = []
    json_data = send_request(substr, None)

    total_titles = int(json_data.get('total'))
    total_pages = int(json_data.get('total_pages'))
    current_page = int(json_data.get('page'))
    for data in json_data.get('data'):
        titles.append(data.get('Title'))

    while current_page < total_pages and len(titles) < total_titles:
        current_page +=1
        json_data = send_request(substr, current_page)
        for data in json_data.get('data'):
            titles.append(data.get('Title'))


def send_request(substr, page):
    base_url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='
    page_query = '&page='+str(page) if page else ''
    request = urlopen(base_url + substr + page_query)
    encoding = request.info().get_content_charset('utf-8')
    response = request.read()
    return json.loads(response.decode(encoding))

f = open('movie_result.txt', 'w')

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
# for res_cur in res:
#     f.write(str(res_cur) + "\n")

f.close()
