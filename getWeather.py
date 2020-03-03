# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:22:51 2020

@author:  Zeren Yan
"""

#--------------Lib----
import requests
import urllib
import json
#from urllib import urlopen


#-----------------INIT---------------
API_KEY='bf28446fa5dc4ab1a5975738202902'
Area='85283'
#Count API call time. every call will be counted by 1.
Track_Amount=0


API_Call='http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+Area

weather = requests.get(API_Call).json()

print(weather)

def get_call_address(API_KEY,Track_Amount,Area):
    pass




'''
Objectives:
    set up a list called AreaList
    
    Set Object Weather. 
    
    Store weather parse into Obj
    
    

'''