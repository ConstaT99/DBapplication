#!/usr/bin/env python3
from wwo_hist import retrieve_hist_data
import os
import numpy as np
import urllib.request as urllib
os.chdir("./")
frequency = 24
start_date = '01-JAN-2013'
end_date = '02-NOV-2020'
api_key = '596f2032f396453b82b235521200211'
My_list = []
for i in range(93100, 94633):
    My_list.append(str(i))
# location_list = ['california']
hist_weather_data = retrieve_hist_data(api_key, My_list, start_date, end_date, frequency, location_label = False, export_csv = True, store_df = True)
