#!usr/bin/python

import sys
import datetime
from influxdb import InfluxDBClient
import os
import time

client=InfluxDBClient('localhost',8086,'admin','admin',database='ANM')
client.create_database('ANM')
def store(sourc_ip,dest_ip,sourc_port,dest_port,rtt,time):
      json=[
              {
              "measurement":"tablename",
              "tags":{
                       "sourc_ip":sourc_ip,
                       "sourc_port":sourc_port,
                       "dest_ip":dest_ip,
                       "dest_port":dest_port
                       },
                       "time":time,
                       "fields":{
                               "RTT":rtt

                       }
      }
      ]
      client.write_points(json,time_precision='u')


f = os.fdopen(sys.stdin.fileno(),'r',0)
for line in f:
    elements = line.strip().split()
    if len(elements) == 6:
        sourc_ip=elements[0]
        sourc_port=elements[1]
        dest_ip=elements[2]
        dest_port=elements[3]

        unixtime = elements[5].split('.')
        stdtime = datetime.datetime.utcfromtimestamp(long(float(unixtime[0]))).strftime('%Y-%m-%dT%H:%M:%S')
        influxtime = ".".join([stdtime,unixtime[1]])
        store(sourc_ip,dest_ip,sourc_port,dest_port,float(elements[4]),influxtime)




