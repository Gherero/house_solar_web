__author__ = 'gherero'
from app import app
from app import controller

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=80)