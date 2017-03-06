#!/bin/bash

echo "Running Spider..."
scrapy runspider spider.py -t json -o - > products.json
echo "Decoding file.."
python decoder.py products.json _business_id
echo "Creating events..."
python import_product.py _business_id
echo "Importing..."
#pio import --appid 4 --input set_events.json
python send_products.py set_events.json 