from flask import Flask
from os import path
import mysql.connector

host="178.79.191.194"
user="maczo_all"
passwd="Pomidor123!@#"
database="hotelowa_db"

db = mysql.connector.connect(
    host= host,
    user=user,
    passwd=passwd,
    database=database,
)



def create_app():

    app = Flask(__name__)
    
    from .sites import views

    app.register_blueprint(views, url_prefix='/')

    return app


