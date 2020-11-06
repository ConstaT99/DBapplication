#!/usr/bin/env python3
from wwo_hist import retrieve_hist_data
import os
import numpy as np
os.chdir("./")
frequency = 24
start_date = '01-JAN-2013'
end_date = '02-NOV-2020'
api_key = '596f2032f396453b82b235521200211'
My_list = ["modesto","moreno-valley","oakland","oceanside","ontario","orange","Oxnard","Palmdale","Pasadena", "Pomona", "rancho-cucamonga", "Riverside", "Sacramento", "Salinas", "san-bernardino", "san-diego", "san-francisco", "san-jose", "santa-ana", "santa-clarita", "santa-rosa", "Stockton", "Torrance"]
# location_list = ['california']
hist_weather_data = retrieve_hist_data(api_key, My_list, start_date, end_date, frequency, location_label = False, export_csv = True, store_df = True)