#!/usr/bin/env python3
import argparse
import io
import sys
from urllib.request import urlopen
import urllib.error
import time
import datetime
from retrying import retry


URL = "http://unreliable.labs.crossref.org/error"

ONE_SECOND=1000
ONE_HOUR=((ONE_SECOND*60)*60)
ONE_DAY=(ONE_HOUR*24)


@retry(wait_exponential_multiplier=1000,wait_exponential_max=(ONE_HOUR * 6))
def fetch(url):
    global s
    d = time.time() - s
    print("time: " + str(d))
    s = time.time()

    try:
        with urlopen(url) as response:
            result = response.read().decode('utf8')
            print("Done fetching...")
            return result
    except urllib.error.URLError as e:
        print("Error: " + str(e))
        raise e

def main():
    print("Starting...")
    print(fetch(ARGS.url))
    print("Done")


s = time.time()    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Stubbornly, but intelligently keep retrying to GET the same URL")
    parser.add_argument("-u", "--url", help="the URL to be stubborn about",
                        type=str, default=URL)
    ARGS = parser.parse_args()
    main()
    
