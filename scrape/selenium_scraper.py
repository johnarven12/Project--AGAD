import csv
from time import sleep
from selenium import webdriver
import pandas as pd

channel = "https://www.youtube.com/user/ANCalerts/videos"#paste your link here
driver = webdriver.Chrome(executable_path='C:/Users/ceejay/Desktop/scrape/chromedriver.exe') #paste the file location where the exec driver is
driver.get(channel)


videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
video_list = []
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    time = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    vid_item = {
    'tittle':title,
    'views':views,
    'posted':time
    }
    video_list.append(vid_item)

df = pd.DataFrame(video_list)

df.to_csv('C:/Users/ceejay/Desktop/scrape/links.csv',index=False) #save to the specified location
driver.quit()
