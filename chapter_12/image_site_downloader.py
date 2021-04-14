from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import requests
import bs4
import os


if len(sys.argv) < 2:
  raise Exception('you have to put a search phrase!')

os.makedirs('./chapter_12/imgur_images', exist_ok=True)

base_url = 'https://imgur.com/'
search_keyword = 'search/score?q='


search_string = ' '.join(sys.argv[1:])


search_url = base_url + search_keyword + search_string
print(search_url)

res = requests.get(search_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

image_list = soup.select('.image-list-link')

for image in image_list:
  image_url = image.get('href').split('/')[2] + '.jpg'
  image_url = base_url + image_url
  res = requests.get(image_url)
  res.raise_for_status()
  
  image_file = open(os.path.join('.\\chapter_12\\imgur_images', os.path.basename(image_url)), 'wb')
  for chunk in res.iter_content(100000):
    image_file.write(chunk)
  image_file.close()