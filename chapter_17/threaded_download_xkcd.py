#! python3
# threaded_download_xkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('./chapter_17/xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
  for url_number in range(start_comic, end_comic):
    # Download the page.
    print('Downloading page https://xkcd.com/%s...' % (url_number))
    res = requests.get('https://xkcd.com/%s' % (url_number))
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
      print('Could not find comic image.')
      
    else:
      comic_url = comic_elem[0].get('src')
      # Download the image.
      print('Downloading image %s...' % (comic_url))
      res = requests.get('https:' + comic_url)
      res.raise_for_status()
      
      # Save the image.
      image_file = open(os.path.join('./chapter_17/xkcd', os.path.basename(comic_url)), 'wb')
      
      for chunk in res.iter_content(100000):
        image_file.write(chunk)
      image_file.close()
      
# Create and start the Thread objects.
download_threads = []
for i in range(0, 140, 10): # loops 14 times, creates 14 threads
  start = i
  end = i + 9
  if start == 0:
    start = 1 # No comic no. 0, so it is set to 1.
  download_thread = threading.Thread(target=download_xkcd, args=(start, end))
  download_threads.append(download_thread)
  download_thread.start()
  
# Wait for all threads to end.
for download_thread in download_threads:
  download_thread.join()
print('Done.')