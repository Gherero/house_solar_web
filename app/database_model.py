from app import *
from datetime import datetime


class Batt_contr(Model):
    voltage = IntegerField()
    datetime = DateTimeField()
    temperature = IntegerField(default=0)

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
