from flask import Flask, render_template
from model import DHTRecord
import json
from optparse import OptionParser
app = Flask(__name__)

def add_parser_options(parser):
	parser.add_option('--port', dest="port",action="store", type="int", default=8080, help="port")
	parser.add_option('--host', dest="host", action="store", type="str", default='0.0.0.0', help="host")
	return parser

def get_records(count=None):
	query_length_limit = 96
	data = None
	if (count is None) or query_length_limit < count < 0:
		data = DHTRecord.query.order_by(DHTRecord.id.desc()).limit(query_length_limit)
	else:
		data = DHTRecord.query.order_by(DHTRecord.id.desc()).limit(count)
	data_array = []
	for element in data:
		data_array.append(element.to_dict())
	return data_array


@app.route('/data/')
@app.route('/data/<int:count>')
def hello(count=None):
	data_array = get_records(count)
	res = json.dumps(data_array)
	return res


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/last')
def last():
	res = DHTRecord.query.order_by(DHTRecord.id.desc()).first().to_json()
	return res


if __name__ == '__main__':
	parser = OptionParser()
	opts, args = parser.parse_args()
	app.run(host=opts.host, port=opts.port)
