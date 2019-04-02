#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:02:52 2018

@author: ejreidelbach

NOTE 1: For the Selenium driver to function properly on Ubuntu, I had to 
        download the most up-to-date geckodriver found at:
        https://github.com/mozilla/geckodriver/releases
            
        Once that is complete, extract the driver and place it in the
        /usr/local/bin folder
       
NOTE 2: An effective selenium guide can be found here:
        https://automatetheboringstuff.com/chapter11/
        
        The relevant contents begin roughly 3/4 down the page. 
"""
 
#==============================================================================
# Package Import
#==============================================================================
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

#==============================================================================
# Function Definitions / Reference Variable Declaration
#==============================================================================
def initiateBrowser(url, headless):
    '''
        Purpose: Initiate a webdriver for scraping web-based data in 
            a headless mode (no visible browser) or with the browser open,
            depending on user-input
    
        Input:   
            (1) url (string): url of website to scrape
            (2) headless (boolean): True if the browser should be run without
                    a browser window (headless), False if the user prefers
                    to have the browser window open
        
        Output: 
            (1) browser (webdriver): browser to be used for webscraping
    '''
    opts = Options()
    opts.headless = headless
    
    # Firefox Setup 
    browser = webdriver.Firefox(options = opts)
    browser.get(url)
    browser.implicitly_wait(100)
    
    return browser
#==============================================================================
# Working Code
#==============================================================================
# Initiate a browser for scraping purposes
browser = initiateBrowser('https://wonder.cdc.gov/mcd-icd10.html', False)

# Click a button on the page
browser.find_element_by_xpath('td/div[2]/ul/li[1]/input').click()  

# Create a select object for interacting with page content
selectAge = Select(browser.find_element_by_xpath('//*[@id="SB_1"]'))
    
# Select an element of the object by using the text visible on the page
selectAge.select_by_visible_text('County')
    
# Select an element of the object by using its underlying value
selectAge.select_by_value('T40.0')