"""
Import sample data for recommendation engine
"""
import random
import predictionio
from datetime import datetime
import pytz
import ujson
import mysql.connector

if __name__ == '__main__':
  exporter = predictionio.FileExporter(file_name="hp_events.json")

  hp_list = ["9788498387568",
            "9788498383621",
            "9788700631625",
            "9780605039070",
            "9788884516374",
            "9780195799163"]
  usr_hp = [1,2,3,4,5]
  count = 0
  for x in xrange(1,100):
    exporter.create_event(
      event="view",
      entity_type="user",
      entity_id="l5;" + str(random.choice(usr_hp)),
      target_entity_type="item",
      target_entity_id="l5;" + random.choice(hp_list),
      event_time=datetime.utcnow().replace(tzinfo = pytz.utc)
    )
    count = count + 1

  for x in xrange(1,20):
    exporter.create_event(
      event="buy",
      entity_type="user",
      entity_id="l5;" + str(random.choice(usr_hp)),
      target_entity_type="item",
      target_entity_id="l5;" + random.choice(hp_list),
      event_time=datetime.utcnow().replace(tzinfo = pytz.utc)
    )
    count = count + 1

  print "%s events are created." % count

  exporter.close()

  exporter = predictionio.FileExporter(file_name="lotr_events.json")

  lotr_list = ["9783608953091",
            "9789633071397",
            "9780261102941"]
  usr_lotr = [6,7,8,9,10]
  count = 0
  for x in xrange(1,100):
    exporter.create_event(
      event="view",
      entity_type="user",
      entity_id="l5;" + str(random.choice(usr_lotr)),
      target_entity_type="item",
      target_entity_id="l5;" + random.choice(lotr_list),
      event_time=datetime.utcnow().replace(tzinfo = pytz.utc)
    )
    count = count + 1

  for x in xrange(1,20):
    exporter.create_event(
      event="buy",
      entity_type="user",
      entity_id="l5;" + str(random.choice(usr_lotr)),
      target_entity_type="item",
      target_entity_id="l5;" + random.choice(lotr_list),
      event_time=datetime.utcnow().replace(tzinfo = pytz.utc)
    )
    count = count + 1
    
  print "%s events are created." % count

  exporter.close()
