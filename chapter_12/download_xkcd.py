#! python3
# download_xkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com' 
os.makedirs('./chapter_12/xkcd', exist_ok=True)
while not url.endswith('#'):
  # Download the page.
  print('Downloading %s... ' % url)
  res = requests.get(url)
  res.raise_for_status()
  
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  
  # Find the URL of the comic image.
  comic_elem = soup.select('#comic img')
  if comic_elem == []:
    print('Could not find comic image.')
  else:
    comic_url = 'https:' + comic_elem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % (comic_url))
    res = requests.get(comic_url)
    res.raise_for_status()
    
    # Save the image to 'xkcd' directory.
    image_file = open(os.path.join('.\\chapter_12\\xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
      image_file.write(chunk)
    image_file.close()
    
    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')
  
print('Done.')