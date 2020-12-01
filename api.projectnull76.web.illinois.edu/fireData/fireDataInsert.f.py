import numpy as np
import pymysql.cursors
import pandas as pd
import sys
sys.path.insert(1, '../')
import dbConnect

connection = dbConnect.mysqlConnect()
cursor = connection.cursor()

cursor.execute('''CREATE TABLE if not exists calFire
        (incidentName varchar(255),
        incidentIsFinal varchar(255),
        incidentDateLastUpdate varchar(255),
        incidentDateCreated varchar(255),
        incidentCounty varchar(255),
        incidentLocation varchar(255),
        incidentAcresBurned varchar(255),
        incidentContainment varchar(255),
        incidentLongitude varchar(255),
        incidentLatitude varchar(255),
        incidentType varchar(255),
        incidentId varchar(255),
        incidentUrl varchar(255),
        incidentDateExtinguished varchar(255),
        incidentDateonlyExtinguished varchar(255),
        incidentDateonlyCreated varchar(255),
        isActive varchar(255),
        calfireIncident varchar(255),
        notificationDesired varchar(255),
        primary key(incidentId))
                ''')

data = pd.read_csv('./data.csv')

data = data.astype(object).replace(np.nan, str("None"))

for row in data.itertuples():
    sql = '''INSERT INTO calFire (incidentName, incidentIsFinal, incidentDateLastUpdate, incidentDateCreated, incidentCounty, incidentLocation, incidentAcresBurned, incidentContainment, incidentLongitude, incidentLatitude, incidentType, incidentId, incidentUrl, incidentDateExtinguished, incidentDateonlyExtinguished, incidentDateonlyCreated, isActive, calfireIncident, notificationDesired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val = (row.incidentName,
           row.incidentIsFinal,
           row.incidentDateLastUpdate,
           row.incidentDateCreated,
           row.incidentCounty,
           row.incidentLocation,
           row.incidentAcresBurned,
           row.incidentContainment,
           row.incidentLongitude,
           row.incidentLatitude,
           row.incidentType,
           row.incidentId,
           row.incidentUrl,
           row.incidentDateExtinguished,
           row.incidentDateonlyExtinguished,
           row.incidentDateonlyCreated,
           row.isActive,
           row.calfireIncident,
           row.notificationDesired)
    # break
    cursor.execute(sql, val)

connection.commit()
