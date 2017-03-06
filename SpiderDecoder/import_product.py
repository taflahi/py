"""
Import sample data for recommendation engine
"""

import predictionio
from datetime import datetime
import pytz
import ujson
import mysql.connector
import sys

if __name__ == '__main__':

  exporter = predictionio.FileExporter(file_name="set_events.json")

  cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='ren')

  cursor = cnx.cursor()

  query = ("SELECT hashid, info, url, business_id from product")
  cursor.execute (query)

  count = 0
  for (hashid, info, url, business_id) in cursor:
    info_string = ujson.loads(info)
    eid = info_string['Code']
    del info_string['Code']
    for key in info_string.keys():
      info_string[key] = [info_string[key]]
    event_properties = info_string
    event_properties["Url"] = ["http://localhost:6001/api/" + hashid]
    event_properties["Slug"] = [url.replace("http://localhost:8000/products/", "")]
    event_properties["businessId"] = [sys.argv[1]]
    exporter.create_event(
      event="$set",
      entity_type="item",
      entity_id=business_id + ";" + eid,
      properties=event_properties,
      event_time=datetime.utcnow().replace(tzinfo = pytz.utc)
    )
    count += 1

  print "%s events are created." % count

  exporter.close()
