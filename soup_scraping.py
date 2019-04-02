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

import requests
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup

#==============================================================================
# Reference Variable Declaration
#==============================================================================
#
#==============================================================================
# Function Definitions
#==============================================================================
def soupifyURL(url):
    '''
    Purpose: Turns a specified URL into BeautifulSoup formatted HTML 

    Input: 
        (1) url (string): Link to the designated website to be scraped
    
    Output: 
        (1) soup (html): BeautifulSoup formatted HTML data stored as a
                complex tree of Python objects
    '''
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    r = session.get(url)
    #r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')   
    return soup

def initializeFolderStructure():
    '''
    Purpose: Create the desired folder structure for all Division 1 football
        teams (1 folder for each team with subfolders for each statistical
        category) in the `data/raw/CFBStats/` folder
        
    Input:
        - NONE
        
    Output:
        - NONE
    '''
    # Create a dictionary of team names and links
    dict_teams = scrapeTeamNames()
    
    for team, url in dict_teams.items():
        directoryCheck(team)
        
    return dict_teams

def directoryCheck(team_name):
    '''
    Purpose: Run a check of the /data/raw/CFBStats/ folder to see if a folder
        exists for the specified team and category. If it doesn't, create it.
        
    Input:
        (1) team_name (string): Name of the school being scraped
    
    Outpu:
        - NONE
    '''
    # Check for the team folder
    pathlib.Path('data/raw/CFBStats/'+team_name).mkdir(parents=True, exist_ok=True)
    
    # Checking for required sub-folders
    for category in ['games', 'players', 'records', 
                     'rosters', 'schedules', 'situations', 'splits']:
        pathlib.Path('data/raw/CFBStats/', team_name, category).mkdir(
                parents=True, exist_ok=True)
    return

#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
path_dir = pathlib.Path('/home/ejreidelbach/Projects/')
os.chdir(path_dir)