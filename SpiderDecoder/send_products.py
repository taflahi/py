import sys
import unirest
import time

with open(sys.argv[1]) as file_object:
	count = 0
	for line in file_object:
		response = unirest.post("http://127.0.0.1:8082/events.json?accessKey=_d1gZbDsJQn-eOTlcxSMZNLzWhoP_CY_9qR7OaqK67qwXEsVCCPTVSjcRNfX-7Qt",
			headers={"Content-Type":"application/json", "Accept": "application/json"},
			params=line)
		count = count + 1
		print(str(count) + ". " + str(response.code))
		time.sleep(0.2);
