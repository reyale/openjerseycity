import urllib2
import json

def get_events(meetup_url):
    # example query
    # https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=Code-For-Jersey-City

    pattern = 'https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=%s' % meetup_url
    data = urllib2.urlopen(pattern).read()
    return json.loads(data)
