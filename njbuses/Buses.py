import os
import datetime
import xml.etree.ElementTree

_sources = {
  'nj': 'http://mybusnow.njtransit.com/bustime/map/getBusesForRouteAll.jsp'
}

class Bus:
  def __init__(self, **kwargs):
     for k,v in kwargs.items():
         setattr(self, k, v)

  def __repr__(self):
     line = []
     for prop,value in vars(self).iteritems():
       line.append((prop,value))
     line.sort(key=lambda x : x[0])
     out_string = ' '.join([k+'='+v for k,v in line]) 
     return 'bus[%s]' % out_string

def parse_xml_data(data):
    results = []

    e = xml.etree.ElementTree.fromstring(data)
    for atype in e.findall('bus'):
        fields = { }
        for field in atype.getchildren():
            if field.tag not in fields and hasattr(field, 'text'):
                if field.text is None:
                    fields[field.tag] = ''
                    continue
                fields[field.tag] = field.text

        results.append(Bus(**fields))
    return results

def get_data(source, raw_dir=None):
    source = source.lower()
    if source not in _sources:
        raise AssertionError('Unknown source=%s valid sources=%s' % (key, str(sources.keys())))

    import urllib2
    data = urllib2.urlopen(_sources[source]).read()
    if raw_dir:
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir)

        now = datetime.datetime.now()
        handle = open(raw_dir + '/' + now.strftime('%Y%m%d.%H%M%S') + '.' + source + '.xml', 'w')
        handle.write(data)
        handle.close()
    return parse_xml_data(data)

def parse_xml_file(fname):
    return parse_xml_data(open(fname,'r').read())
