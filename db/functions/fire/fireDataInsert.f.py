import numpy as np
import pymysql.cursors
import pandas as pd

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Teamnull',
                             db='projectnull',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


data = pd.read_csv ('../../../data/fireData/data.csv')

data = data.astype(object).replace(np.nan, str("None"))

for row in data.itertuples():
    sql = '''INSERT INTO calFire (incidentName, incidentIsFinal, incidentDateLastUpdate, incidentDateCreated, incidentCounty, incidentLocation, incidentAcresBurned, incidentContainment, incidentLongitude, incidentLatitude, incidentType, incidentId, incidentUrl, incidentDateExtinguished, incidentDateonlyExtinguished, incidentDateonlyCreated, isActive, calfireIncident, notificationDesired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val = ( row.incidentName,
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
    cursor.execute(sql,val)

connection.commit()
