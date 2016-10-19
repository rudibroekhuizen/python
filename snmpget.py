#!/usr/bin/env python

import yaml
import subprocess
import json

with open('data.yml') as yml_file:
    config = yaml.load(yml_file)

for device_config in config['devices']:
    host = device_config['host']
    community = device_config['community']
    devicegroup = device_config['devicegroup']
    for metric_config in device_config['metrics']:
        oid = metric_config['oid']
        name = metric_config['name']
        p = subprocess.Popen(['snmpget','-v','2c','-c',community,'-Ln','-Otqv',host,oid],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
        out, err = p.communicate()
        obj = {'host': host, 'devicegroup': devicegroup, name: out.rstrip('\n')}
        print(json.dumps(obj, separators=(', ',': ')))
