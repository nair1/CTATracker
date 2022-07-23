from re import L

class RequestInfo():
    API_KEY = 'ae58d07673eb4bf4ae59f9c0a288c470'

    BASE_URL = 'http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?'

class Lines():
    BLUE = ['blue', 'Blue']
    BROWN = ['brn', 'Brown']
    GREEN = ['g', 'Green']
    ORANGE = ['org', 'Orange']
    PINK = ['pink', 'Pink']
    PURPLE = ['p', 'Purple']
    RED = ['red', 'Red']
    YELLOW = ['y', 'Yellow']

    ALL = [BLUE, BROWN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW]

class Constants():
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'