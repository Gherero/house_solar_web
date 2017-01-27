__author__ = 'gherero'
from app.database_model import *
from flask import Flask
from peewee import *
from datetime import datetime



db = SqliteDatabase('house.db')
db.connect()
if not Batt_contr.table_exists():
    Batt_contr.create()

app = Flask(__name__)
app.config.from_object('config')


from app import controller