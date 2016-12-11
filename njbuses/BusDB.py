import os
import sqlite3

_columns = [ 'lat',
 'lon',
 'ar',
 'bid',
 'c',
 'cars',
 'consist',
 'd',
 'dd',
 'dn',
 'fs',
 'id',
 'm',
 'op',
 'pd',
 'pdRtpiFeedName',
 'pid',
 'rt',
 'rtRtpiFeedName',
 'rtdd',
 'rtpiFeedName',
 'run',
 'wid1',
 'wid2']

_create_db_string = '''CREATE TABLE buses (pkey integer primary key autoincrement, lat real, lon real, ar text, bid text, c text, cars text, consist text, d text, dd text, dn text, fs text, id text, m text, op text, pd text, pdRtpiFeedName text, pid text, rt text, rtRtpiFeedName text, rtdd text, rtpiFeedName text, run text, wid1 text, wid2 text, timestamp text)'''

_insert_string = 'INSERT INTO buses VALUES(NULL, %f, %f, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' 

def _bus_to_sql(bus, timestamp):
    for var in _columns: 
        if not hasattr(bus, var):
            setattr(bus, var, '')
 
    return _insert_string % (float(bus.lat), float(bus.lon), bus.ar, bus.bid, bus.c, bus.cars, bus.consist, bus.d, bus.dd, bus.dn, bus.fs, bus.id, bus.m, bus.op, bus.pd, bus.pdRtpiFeedName, bus.pid, bus.rt, bus.rtRtpiFeedName, bus.rtdd, bus.rtpiFeedName, bus.run, bus.wid1, bus.wid2, str(timestamp)) 

class BusDB:
    def _execute(self, command):
        self._batch_execute([command])

    def _batch_execute(self, commands):
        cursor = self.conn.cursor()
        for command in commands:
            cursor.execute(command)
        self.conn.commit()

    def __init__(self, fname):
        self.conn = None
        self.fname = fname

        if not os.path.exists(self.fname):
            if not os.path.exists(os.path.dirname(self.fname)):
                os.makedirs(os.path.dirname(self.fname))
            self.conn = sqlite3.connect(self.fname)
            self._execute(_create_db_string)
        else:
            self.conn = sqlite3.connect(self.fname)

    def insert_buses(self, buses, timestamp):
        self._batch_execute([_bus_to_sql(b, timestamp) for b in buses])

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
