                                                          ReadMe
_____________________________________________________________________________________________________________________________________________


This program is designed in Python environment.For the capturing stream it is integrated with CAP2PCAP utility and tshark.then output will be stored in influxdb directly.

Installation:

1.First you need to clone DPMI utils from "https://github.com/suhaila94/libcap_utils"
2.See Installing for details.

	autoreconf -si
	mkdir build; cd build
	../configure 
	make
	sudo make install

3.install Grafana as shown bellow
	

	$ wget https://grafanarel.s3.amazonaws.com/builds/grafana_3.1.1-1470047149_amd64.deb
	$ sudo apt-get install -y adduser libfontconfig
	$ sudo dpkg -i grafana_3.1.1-1470047149_amd64.deb

4.install influxdb as shown bellow

	curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
	source /etc/lsb-release
	echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

5.install tshark as shown bellow

	sudo apt-get install tshark

6.install Flask as shown bellow 

	sudo pip install Flask


Usage:

This tool is designed for calculating 

                    1.RTT values of raw data
                    2.RTT values of source and destination port
                    3.RTT values of source and destination IP.

 These values are plotted in grafana by grouping technique.


RestApi manual:

we are provided different ficilities to analiza stream statistics.

1.Run stream 

	curl http://localhost:5000/run/stream1_stream_2 ....

2.Change stream

	curl http://localhost:5000/run/stream1_stream_2 ....

3.Stop stream

	curl http://localhost:5000/stop

4.Show active streams

	curl http://localhost:5000/showstream

5.Add stream

	curl http://localhost:5000/add/stream1_stream_2 ....

6.Delete stream

	curl http://localhost:5000/delete/stream1_stream_2 ....



___________________________________________________________________________________________________________________________________________
