#!/usr/bin/python

import dload
from subprocess import call
import sys, getopt

def get_jsonparsed_data(url, index):
    return dload.json(url)[index]

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def print_stats(title, stats):

    """
    Print stats from a dict to a table

    Parameters
    ----------
    title : str
    stats : dict

    """
    print('{:^33}'.format(title.title()))
    print('{:_<33}'.format(''))

    for x, y in stats.items():
        print('{:15}'.format(x.title()), '{:>15}'.format(y), sep=" | ", flush=True)

def get_country_dict(country):
    #Data of Countries
    nations_url = 'https://pkgstore.datahub.io/core/covid-19/countries-aggregated_json/data/8b23d87cfcb28e7ee2f4a92633821d6d/countries-aggregated_json.json'

def get_world_dict():
    # Data from World Wide jsom
    world_url = 'https://pkgstore.datahub.io/core/covid-19/worldwide-aggregated_json/data/eeb678cc915ff4adc3dc01638312f766/worldwide-aggregated_json.json'
    latest_dict = get_jsonparsed_data(world_url, -1)
    # Truncate the increase rate
    latest_dict["Increase rate"] = truncate(latest_dict["Increase rate"], 4)
    return latest_dict

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc", ["country="])
    except getopt.GetoptError:
        print('usage: covid-19-status.py [-h] [-c COUNTRY]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('covid-19-status.py [-h] [-c COUNTRY]')
            sys.exit();
        elif opt in ("-c", "--country"):
            print(argv[1])

    if not argv:
        call('clear')
        print_stats("Covid-19 Stats", get_world_dict())

if __name__ == "__main__":
   main(sys.argv[1:])
