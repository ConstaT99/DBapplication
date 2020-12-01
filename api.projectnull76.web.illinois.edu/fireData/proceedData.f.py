import pandas as pd
import numpy as np

fire = pd.read_csv("WildFireData.csv")

wildFire = fire[fire.incident_type == 'Wildfire']

#change incident_Id to incidentId
newNames = ['incidentName', 'incidentIsFinal', 'incidentDateLastUpdate', 'incidentDateCreated', 'incidentAdministrativeUnit', 'incidentAdministrativeUnitUrl', 'incidentCounty', 'incidentLocation', 'incidentAcresBurned', 'incidentContainment', 'incidentControl', 'incidentCooperatingAgencies', 'incidentLongitude', 'incidentLatitude', 'incidentType', 'incidentId', 'incidentUrl', 'incidentDateExtinguished', 'incidentDateonlyExtinguished', 'incidentDateonlyCreated', 'isActive', 'calfireIncident', 'notificationDesired']
wildFire.columns = newNames

# change indecident date
dateindex = wildFire.index
dateindex2 = wildFire.columns.get_loc("incidentDateonlyCreated")
wildFire.loc[:,'incidentDateonlyCreated'] = pd.to_numeric(wildFire.incidentDateonlyCreated.str.replace('-',''))
# print(wildFire)
# wildFire.to_csv('data.csv')
# incidentCountyvalues = []
# for i in wildFire.loc[:,'incidentCounty']:
#     incidentCountyvalues.append(i.split(", "))
# wildFire.loc[:,'incidentCounty'] = incidentCountyvalues
wildFire.to_csv('data.csv')


