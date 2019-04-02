#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:41:13 2019

@author: ejreidelbach

:DESCRIPTION:

:REQUIRES:
   
:TODO:
"""
 
#==============================================================================
# Package Import
#==============================================================================
import os  
import pandas as pd
import pathlib
import tqdm

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

#==============================================================================
# Reference Variable Declaration
#==============================================================================
#
#==============================================================================
# Function Definitions
#==============================================================================
def initiateBrowser(url, headless):
    '''
    Purpose: Initiate a webdriver for scraping web-based data in a headless 
        mode (no visible browser) or with the browser open, depending on 
        user-input

    Inputs   
    ------
        url : string
            url of website to scrape
        headless : boolean
            True if the browser should be run without a browser window 
            False if the user prefers to have the browser window open
    
    Outputs
    -------
        browser : webdriver
            browser to be used for webscraping
    '''
    opts = Options()
    opts.add_argument('headless')
    #opts.headless = headless 
    
    # Firefox Setup 
#    prof = webdriver.FirefoxProfile()
#    prof.set_preference("javascript.enabled", False)
#    browser = webdriver.Firefox(options = opts, firefox_profile = prof)
#    browser.get(url)
#    browser.implicitly_wait(100)
    
    # Chrome setup
    browser = webdriver.Chrome(options = opts)
    browser.get(url)
    #browser.implicitly_wait(100)

    # Click the 'I Agree' button 
    try:
        button_agree = browser.find_element_by_xpath(
                str('/html/body/div[2]/div[1]/div/div/div/div/div/' + 
                'form/div[3]/div[2]/center/input'))
        button_agree.click()
    except:
        pass
    return browser

def runScrapingProcess(browser, deathType):
    '''
        Purpose:
                    
        Inputs
        ------
            (1)
                    
        Outputs
        -------
            (1)
    '''
    #--------------------------------------------------------------------------
    #   Begin the scraping process!
    #--------------------------------------------------------------------------     
    # Use beautifulSoup to extract data from the generated page
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', {'class':'response-form'})
    
    # shutdown the browser once we're done scraping
#    browser.close()
    browser.quit()
    
    return
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
path_dir = pathlib.Path('/home/ejreidelbach/Projects/')
os.chdir(path_dir)

# Start the browser without a browser window for Multiple Causes of Death
browser = initiateBrowser('https://wonder.cdc.gov/mcd-icd10.html', False)
# Scrape data for `Multiple` causes
runScrapingProcess(browser, 'Multiple')