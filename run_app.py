#!/usr/bin/env python
import server
import record_data
from optparse import OptionParser

if __name__ == "__main__":
	usage = "you can find options info in server.py and record_data.py or by calling this script with -h options"
	parser = OptionParser(usage=usage)
	parser = server.add_parser_options(parser)
	parser = record_data.add_parser_options(parser)
	opts, args = parser.parse_args()
	sensor = record_data.sensor_args[opts.s]
	sd = record_data.SensorDatabase(opts.pin, sensor, opts.t, opts.p)
	sd.daemon = True
	sd.start()
	print "serwer running"
	server.app.run(host=opts.host, port=opts.port)