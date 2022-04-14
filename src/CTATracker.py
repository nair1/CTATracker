from xmlrpc.client import ResponseError
from Constants import *

import requests
import json

from datetime import datetime
from datetime import timedelta

def main():
    for route in Lines.ALL:
        print_all_train_info(route)
    
def get_url(route_color):
    url = RequestInfo.BASE_URL

    url += 'key=' + RequestInfo.API_KEY
    url += '&rt=' + route_color
    url += '&outputType=JSON'

    return url

def get_train_info(response):
    route_info = response.json()['ctatt']['route'][0]

    if 'train' not in route_info:
        return None
    elif not isinstance(route_info['train'], list):
        return [route_info['train']]

    return route_info['train']

def print_all_train_info(route_color):
    url = get_url(route_color[0])
    response = requests.get(url)

    if not response.ok:
        raise ResponseError('Error: response did not resolve okay!')

    train_info = get_train_info(response)
    
    print(route_color[1] + ' Line Info:')

    for train in train_info:
        current_time = datetime.strptime(train['prdt'], Constants.DATE_FORMAT)
        arrival_time = datetime.strptime(train['arrT'], Constants.DATE_FORMAT)
        
        time_to_arrival = arrival_time - current_time
        minutes_to_arrival = int(time_to_arrival.total_seconds() / 60)
        
        print(str(minutes_to_arrival) + ' min - ' + train['nextStaNm'] + ' heading towards ' + train['destNm'])

    print('\n')

if __name__ == "__main__":
    main()