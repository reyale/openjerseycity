import xml.etree.ElementTree

_sources = {
  'nj': 'http://mybusnow.njtransit.com/bustime/map/getBusesForRouteAll.jsp'
}

class Bus:
  def __init__(self, id_text, lat, lon, headsign, destination, timestamp):
     self.id_text = id_text
     self.lat = lat
     self.lon = lon
     self.headsign = headsign
     self.destination = destination
     self.timestamp = timestamp

  def __repr__(self):
     # need to format the time better?
     return 'bus[id=%s lat=%s long=%s headsign=%s destination=%s time=%s]' % (self.id_text, self.lat, self.lon, self.headsign, self.destination, self.timestamp)

def parse_xml_data(data):
    results = []

    e = xml.etree.ElementTree.fromstring(data)
    for atype in e.findall('bus'):
        ids = atype.findall('id')
	if len(ids) != 1:
	    continue
	id_text = ids[0].text

	lats = atype.findall('lat')
	if len(lats) != 1:
	    continue
	lat = lats[0].text

	lons = atype.findall('lon')
	if len(lons) != 1:
            continue
        lon = lons[0].text

    headsign = atype.findall('fs')
    if len(fs) != 1:
            continue
        headsign = fs[0].text

    destination = atype.findall('pd')
    if len(pd) != 1:
            continue
        destination = pd[0].text

    timestamp = mark

    results.append(Bus(id_text, lat, lon, headsign, destination, timestamp))
    return results

def get_data(source):
    source = source.lower()
    if source not in _sources:
        raise AssertionError('Unknown source=%s valid sources=%s' % (key, str(sources.keys())))

    # mark the time right before we fetch the source data
    import datetime
    mark = datetime.datetime.now()
    
    import urllib2
    data = urllib2.urlopen(_sources[source]).read()
    return parse_xml_data(data), mark

def parse_xml_file(fname):
    return parse_xml_file(open(fname,'r').read())
