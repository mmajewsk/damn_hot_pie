from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import sqlite3
import json
import os


app = Flask(__name__)
script_path = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+script_path+'/dht_database.db'
db = SQLAlchemy(app)

class DHTRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Integer())
    temperature = db.Column(db.Integer())
    date = db.Column(db.DateTime())

    def __init__(self, humidity, temperature, date):
        self.humidity = humidity
        self.temperature = temperature
        self.date = date

    def __repr__(self):
        return 'H:{0},T:{1},DateTime:{2}\n'.format(self.humidity, self.temperature, self.date)

    def to_dict(self):
        d = {}
        d["id"] = self.id
        d["humidity"] = self.humidity
        d["temperature"] = self.temperature
        d["date"] = str(self.date)
        return d

    def to_json(self):
        d = self.to_dict()
        return json.dumps(d)

try:
    DHTRecord.query.first()
except sqlalchemy.exc.OperationalError as e:
    #print app.config['SQLALCHEMY_DATABASE_URI']
    db.create_all()
