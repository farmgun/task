import pandas as pd
df=input()
df
import googlemaps

gmaps_key=googlemaps.Client(key="AIzaSyBSOAyzUhtvTIdNxI_gc7aji3en8irUgps")
df["LAT"]=None
df["LON"]=None

for i in range(0,len(df),1):
    geocode_result-gmaps_key.geocode(df.iat[i,0])
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lat"]
        df.iat[i,df.columns.get_loc("LAT")]=lat
        df.iat[i,df.columns.get_loc("LON")]=lot
    except:
        lat=None
        lon=None
