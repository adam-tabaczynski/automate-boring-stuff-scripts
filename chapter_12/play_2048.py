from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
direction_tuple = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
other_dir_tuple = (Keys.LEFT, Keys.RIGHT, Keys.DOWN)
game_table_elem = browser.find_element_by_tag_name('html')
game_scores = []
games = 0
while True:
  for direction in direction_tuple:
    game_table_elem.send_keys(direction)
    time.sleep(0.001)

  try:
    end_elem = browser.find_element_by_class_name('game-over')
    score_elem = browser.find_element_by_class_name('score-container')
    game_scores += [score_elem.text]
    browser.refresh()
    time.sleep(1)
    game_table_elem = browser.find_element_by_tag_name('html')
    print(score_elem.text)
    games += 1
    print(games)
    if games > 3:
      break
  
  except:
    pass
  
for score in game_scores:
  print(score)

time.sleep(30)