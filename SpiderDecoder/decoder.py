import sys
import ujson
import mysql.connector
from hashids import Hashids

with open(sys.argv[1]) as json_file:

	if len(sys.argv) < 3:
		sys.exit()

	links = ujson.load(json_file)

	link_dict = {}

	for link in links:
		url = link['Url']

		product = {}
		for key in link.keys():
			if(key != 'Url'):
				product[key] = link[key]
		
		link_dict[url] = ujson.dumps(product)

	hashids = Hashids()
	cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='ren')

	cursor = cnx.cursor()

	query = ("SELECT url from product")
	add_product = ("INSERT INTO product "
	               "(url, info, status, business_id) "
	               "VALUES (%s, %s, %s, %s)")
	update_hash = ("UPDATE product set hashid = %s where id = %s")
	update_status_by_url = ("UPDATE product set status = %s where url = %s")

	# find diff between old list and new list
	cursor.execute (query)

	urlist = []
	for (url) in cursor:
		urlist.append(url[0])

	nwlist = list(link_dict.keys())

	sett0 = set(urlist) - set(nwlist)
	sett0 = list(sett0)

	sett1 = set(nwlist) - set(urlist)
	sett1 = list(sett1)

	print(sett0)
	print(sett1)

	# set this old list status to 0
	for url in sett0:
		cursor.execute(update_status_by_url, (0, url))

	for url in sett1:
		cursor.execute(add_product, (url, link_dict[url], 1, sys.argv[2]))
		pid = cursor.lastrowid
		hashed = hashids.encode(pid)
		cursor.execute(update_hash, (hashed, pid))

	cnx.commit()

	cursor.close()
	cnx.close()