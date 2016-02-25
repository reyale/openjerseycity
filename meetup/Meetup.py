import urllib2
import json

def get_events(meetup_url, max_results=None):
    # example query
    # https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=Code-For-Jersey-City

    pattern = 'https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=%s' % meetup_url

    if max_results is not None:
        int(max_results) # cause it to bomb if it's not an int
        pattern += '&page=' + str(max_results) 

    data = urllib2.urlopen(pattern).read()
    return json.loads(data)
