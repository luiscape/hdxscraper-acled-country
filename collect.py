#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from collector.parser import parse
from collector.countries import collect_countries
from collector.register import create_datasets, create_resources, create_gallery_items


def main():
    '''
    Wrapper.

    '''
    countries = collect_countries()
    parsed_data = parse(countries)

    create_datasets(datasets=parsed_data['datasets'],
        hdx_site='http://data.hdx.rwlabs.org', apikey=os.getenv('HDX_KEY'))

    create_resources(resources=parsed_data['resources'],
        hdx_site='http://data.hdx.rwlabs.org', apikey=os.getenv('HDX_KEY'))

    create_gallery_items(gallery_items=parsed_data['gallery_items'],
        hdx_site='http://data.hdx.rwlabs.org', apikey=os.getenv('HDX_KEY'))

if __name__ == '__main__':
    main()
