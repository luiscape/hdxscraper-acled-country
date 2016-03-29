#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COUNTRIES:
---------

Collects lists of countries from the ACLED website.

'''
import requests

from bs4 import BeautifulSoup
from countrycode.countrycode import countrycode

def collect_countries():
    '''
    Collects lists of countries and links from
    ACLED's website.

    '''
    u = 'http://www.acleddata.com/data/version-6-data-1997-2015/'
    level = 7
    r = requests.get(u)

    soup = BeautifulSoup(r.content, 'html.parser')
    x = soup.findAll('ul')

    countries = []
    for l in x[level]:
        if len(l) == 2:
            countries.append({
                'name': l.get_text().replace(' (xls)', ''),
                'url': l.findAll('a')[0].get('href'),
                'iso': countrycode(l.get_text().replace(' (xls)', ''), 'country_name', 'iso3c').lower()
            })

    return countries
