#!flask/bin/python

import sys
import socket
import threading
from flask import Flask
from flask import send_file
import os
import time
from multiprocessing import Process
import subprocess, shlex


app = Flask(__name__)



#DPMI strings 
@app.route('/run/<string:stream>', methods = ['GET'])
def start_process(stream):
        address = stream.split('_')
        global gstream
        gstream = ' '.join(address)
        Process(target = start_king(stream)).start()
        return "please wait........"

#stop DPMI utils

@app.route('/stop', methods=['GET'])
def stop_service():
         os.system("sudo kill -9 $(pgrep cap2pcap)")
#pkill -f cap2pcap
         return "DPMI stoped\n"

#add New stream

@app.route('/add/<string:NewStream>', methods=['GET'])
def add_stream(NewStream):

#       gstream=start_process(stream)
	address = NewStream.split('_')
	addstream = ' '.join(address)
        stop_service()
        time.sleep(3)
        start_process(gstream+' '+addstream)
        return "stream added\n"

#delete stream

@app.route('/delete/<string:deletestream>', methods=['GET'])
def delete_stream(deletestream):
		 address = deletestream.split('_')
		 delstream = ' '.join(address)
                 NewStream = gstream.replace(delstream,'')
                 stop_service()
                 time.sleep(3)
                 start_process(NewStream)
                 return "stream deleted\n"


@app.route('/showstream', methods=['GET'])
def show_service():
#pkill -f myName
         return gstream


#change stream
@app.route('/change/<string:changestream>', methods=['GET'])
def new_stream(changestream):
        try:
             stop_service()
             time.sleep(3)
             start_process(changestream)
        except:
             print ""
        return "stream changed\n"

def start_king(stream):
        dpmi(stream).start()
        return "please wait \n"



# Piping done two types  which is using subprocess or exicute commands directly throuth os.system

#def subprocess_cmd(command):
#    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
#    proc_stdout = process.communicate()[0].strip()
#    print proc_stdout


def start_service(stream):
        os.system("sudo cap2pcap -i eth1 "+gstream+" |tshark -r -  -Y ' tcp.analysis.ack_rtt' -Tfields -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e tcp.analysis.ack_rtt -e frame.time_epoch | python influx.py")


class dpmi(threading.Thread):
        def __init__(self,stream):
              threading.Thread.__init__(self)
              self.stream = stream
        def run(self):
            start_service(self.stream)


if __name__=='__main__':
       app.run(host ='0.0.0.0')




