
import json
import csv

config = dict()

config['refresh'] = '300' # 300 Seconds: 5 Minutes
config['title'] = "Server status dashboard"
config['tasks'] = []

with open('vms.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
         config['tasks'].append({'id': row[0],
                                 'title': row[1],
                                 'type': 'shell',
                                 'command': 'ping -c 1 %s' % row[2],
                                 'group-id': row[3],
                                 })
            
            

with open('config.json', 'w') as outfile:
    json.dump(config, outfile, indent=4)