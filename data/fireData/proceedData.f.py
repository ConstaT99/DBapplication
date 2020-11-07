import pandas as pd
import numpy as np

fire = pd.read_csv("WildFireData.csv")

wildFire = fire[fire.incident_type == 'Wildfire']
# date = wildFire.incident_dateonly_created
dateindex = wildFire.index
dateindex2 = wildFire.columns.get_loc("incident_dateonly_created")
# print(dateindex2)
# for i in dateindex:
# print(type(wildFire.incident_dateonly_created[1]))
wildFire['incident_dateonly_created'] = pd.to_numeric(wildFire.incident_dateonly_created.str.replace('-',''))
# print(wildFire[wildFire.incident_dateonly_created == 20090524])
wildFire.to_csv('data.csv')
