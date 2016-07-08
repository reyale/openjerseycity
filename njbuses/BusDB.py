import os
import sqlite3

def _bus_to_sql(bus):
    return 'INSERT INTO buses VALUES(NULL, "%s", %f, %f, "%s", "%s", "%s")' % (bus.id_text, float(bus.lat), float(bus.lon), bus.headsign, bus.destination, str(bus.timestamp))

class BusDB:
    def _execute(self, command):
        self._batch_execute([command])

    def _batch_execute(self, commands):
        cursor = self.conn.cursor()
        for command in commands:
            print command
            cursor.execute(command)
        self.conn.commit()

    def __init__(self, fname):
        self.conn = None
        self.fname = fname

        if not os.path.exists(self.fname):
            if not os.path.exists(os.path.dirname(self.fname)):
                os.makedirs(os.path.dirname(self.fname))
            self.conn = sqlite3.connect(self.fname)
            self._execute('''CREATE TABLE buses (id integer primary key autoincrement, bus_id text, lat real, lon real, headsign text, destination text, timestamp text)''')
        else:
            self.conn = sqlite3.connect(self.fname)

    def insert_buses(self, buses):
        self._batch_execute([_bus_to_sql(b) for b in buses])

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
