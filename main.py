# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
import time
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable
from sys import platform


def worker_thread(search_key, directory_name):
    start_time = time.time()

    image_scraper = GoogleImageScraper(
        webdriver_path, image_path, search_key, directory_name, number_of_images, headless, min_resolution, max_resolution, max_missed)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames, 224, 224)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  

    #Release resources
    del image_scraper

    if(platform == 'darwin'):
        os.system("afplay /System/Library/Sounds/Glass.aiff")

if __name__ == "__main__":

    #timer
    start_time = time.time()

    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    
    # Read attractions.txt and add to set
    keys = []
    values = []
    count = 0
    path = "../places.txt"
    eng = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:

            # 0 is English name, 1 is Thai name
            eng = line.split("==")[0]
            thai = line.split("==")[1]
            values.append(eng.strip().lower())
            keys.append(thai.strip())


    search_keys = keys
    directory_name = values


    #Parameters
    number_of_images = 1                # Desired number of images
    headless = True                     # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (1920, 1080)       # Maximum desired image resolution
    max_missed = 1000                   # Max number of failed images before exit
    number_of_workers = 1               # Number of "workers" used
    keep_filenames = False              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys, directory_name)


    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  

    if(platform == 'darwin'):
        os.system("afplay /System/Library/Sounds/Glass.aiff")
