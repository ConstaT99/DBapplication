import pandas as pd
import numpy as np

fire = pd.read_csv("WildFireData.csv")
wildFire = fire[fire.incident_type == 'Wildfire']
wildFire.to_csv('data.csv')