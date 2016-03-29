#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
PARSER:
------

Parser of scraper data in to HDX-ready data.

'''
from copy import copy
from slugify import slugify

def parse(objects):
    '''
    This parses data.

    '''
    dataset = {
        'name': None,
        'title': None,
        'owner_org': 'acled',
        'author': 'acled',
        'author_email': 'c.raleigh@acleddata.com',
        'maintainer': 'acled',
        'maintainer_email': 'c.raleigh@acleddata.com',
        'license_id': 'cc-by-sa',
        'dataset_date': '01/01/1997-12/31/2015',  # has to be MM/DD/YYYY
        'subnational': 1,  # has to be 0 or 1. Default 1 for ACLED.
        'notes': """ACLED makes its dataset of disaggregated conflict and protest data publicly available. A new version of the dataset is released annually, with data from the previous year and targeted quality review being added in each new version. Files for all countries are composed of ACLED events which indicate the day, actors, type of activity, location, fatalities, sources and notes for individual politically violent events. Please see the [codebook](http://www.acleddata.com/wp-content/uploads/2016/01/ACLED_Codebook_2016.pdf) for further details on conflict categories, actors, events and sources. The [user guide](http://www.acleddata.com/wp-content/uploads/2016/01/ACLED_User-Guide_2016.pdf) provides guidance on downloading and reading files. <br />ACLED data are presented in three forms: the first is an Excel for the entire African continent; the second is a corresponding shapefile of the African continent created from those data; the third format is an Excel file called “COUNTRY X” containing data disaggregated by country which occur in the named state’s territory (including foreign groups active in a state’s territory).""",
        'caveats': "Most data analysis can be carried out using the standard Excel file. In this file, both Actor 1 and Actor 2 appear in the same row, with each event constituting a single unit of analysis. However, in order to analyse conflict actors and actor types, a monadic file is more useful. This is a file in which Actor 1 and Actor 2 appear in a single column, with each actor’s activity constituting a single unit of analysis. This allows users to analyse different trends and patterns, like the proportion of events in which a particular actor or actor type is involved; or the geographic patterns of activity of specific actors. Creating a monadic file involves duplicating the events so that each actor is represented as participating in a single event (almost doubling the number of events in the dataset). For this reason, monadic files are not useful for analysis of the number of events or overall patterns of violence in a country, etc. They should be used for analysis of actors, actor types and patterns in their activity. The dyadic actor file allows analysis on specific actors within the dataset. Actor 1 and Actor 2 are each assigned a unique actor ID and the actor dyad column represents the two actors involved in each event. This allows users to analyse the number of events; number of fatalities; type of event; or geographic location of events in which two discrete actors interact, for example, events involving Boko Haram and the Military Forces of Nigeria.",
        'data_update_frequency': '30',
        'methodology': 'Other',
        'methodology_other': "This page contains information about how the ACLED team collects, cleans, reviews and checks event data, with a focus on what makes ACLED unique and compatible with other data. The process of ACLED coding assures that it is accurate, comprehensive, transparent and regularly updated. ACLED-Africa data is available from 1997 and into real time. ACLED-Asia produces publicly available real-time data and continues to backdate for all states. Data will be posted as it is complete.  For more information about its methodology, please consult [ACLED's Methodology page](http://www.acleddata.com/methodology/).",
        'dataset_source': 'ACLED',
        'package_creator': 'luiscape',
        'private': False,  # has to be True or False
        'url': None,
        'state': 'active',  # always "active".
        'tags': [{ 'name': 'conflict' }, { 'name': 'political violence' }, { 'name': 'protests' }, { 'name': 'war' }],
        'groups': []  # has to be ISO-3-letter-code. { 'id': None }
    }

    resource = {
        'package_id': None,
        'url': None,
        'name': None,
        'format': 'xlsx',
        'description': None
    }

    gallery_item = {
        'title': 'Dynamic Map: Political Conflict in Africa',
        'type': 'visualization',
        'description': 'The dynamic maps below have been drawn from ACLED Version 6. They illustrate key dynamics in event types, reported fatalities, and actor categories. Clicking on the maps, and selecting or de-selecting options in the legends, allows users to interactively edit and manipulate the visualisations, and export or share the finished visuals. The maps are visualised using Tableau Public.',
        'url': 'http://www.acleddata.com/visuals/maps/dynamic-maps/',
        'image_url': 'http://docs.hdx.rwlabs.org/wp-content/uploads/acled_visual.png',
        'dataset_id': None
    }

    datasets = []
    resources = []
    gallery_items = []

    for object in objects:
        dataset['name'] = slugify('ACLED Conflict Data for %s' % object['name'])
        dataset['title'] = 'ACLED Conflict Data for %s' % object['name']
        dataset['groups'] = [{ 'id': object['iso'] }]

        resource['package_id'] = slugify('ACLED Conflict Data for %s' % object['name'])
        resource['name'] = object['url'].rsplit('/', 1)[-1]
        resource['url'] = object['url']

        gallery_item['dataset_id'] = slugify('ACLED Conflict Data for %s' % object['name'])

        datasets.append(copy(dataset))
        resources.append(copy(resource))
        gallery_items.append(copy(gallery_item))

    return {
        'datasets': datasets,
        'resources': resources,
        'gallery_items': gallery_items
        }
