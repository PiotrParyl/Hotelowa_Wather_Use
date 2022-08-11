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







#==================== functions ==========================


def select_value_db(select_what,select_from,select_howmany,):
    
    mycursor = db.cursor()

    mycursor.execute(f"SELECT {select_what} FROM {select_from} ORDER BY id DESC LIMIT {select_howmany}")

    resoult = mycursor.fetchall()

    test_list = []
    value_list = []

    for i in resoult:
        test_list.append(i)
        

    for i in range(0,len(test_list)):
        value= list(f"{test_list[i]}")

        del value[0:1]
        del value[-2:]
        
        joined = "".join(value)

        value_list.append(joined)


    return value_list


def water_use_per_hour(hours):
    x = hours * 60
    z = x/5
    z = int(z)

    chuj = select_value_db("value","water_use",z)
    wynik = float(chuj[0])- float(chuj[-1])
    return wynik