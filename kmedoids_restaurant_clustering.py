import requests
from pyclustering.cluster import kmedoids
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils import read_sample
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import csv
import pandas as pd

capoluoghi = [
    ["Aosta", 45.7349551, 7.3130762],
    ["Torino", 45.0703121, 7.6868565],
    ["Genova", 44.4056499, 8.946256],
    ["Milano", 45.4667971, 9.1904984],
    ["Trento", 46.0664228, 11.1257601],
    ["Venezia", 45.438759, 12.327145],
    ["Trieste", 45.6495264, 13.7768182],
    ["Bologna", 44.4936714, 11.3430347],
    ["Firenze", 43.7698712, 11.2555757],
    ["Ancona", 43.6170136, 13.5170982],
    ["Perugia", 43.1107009, 12.389172],
    ["Roma", 41.9027835, 12.4963655],
    ["L'Aquila", 42.3498993, 13.3995089],
    ["Campobasso", 41.560695, 14.6620492],
    ["Napoli", 40.8521771, 14.2681252],
    ["Bari", 41.1257843, 16.8620293],
    ["Potenza", 40.6420026, 15.7998552],
    ["Catanzaro", 38.905975, 16.5944015],
    ["Palermo", 38.11569725, 13.3623567],
    ["Cagliari", 39.2153118, 9.1106163]
]

data_list = []
data_info=[]
valutazione =[]

def caricoArray(latitudine,longitudine):
  url = "https://api.content.tripadvisor.com/api/v1/location/nearby_search?latLong={}%2C{}&key=4CC76D5579094823A20D1BA66DCA0BC7&radius=10&radiusUnit=km&language=en".format(latitudine,longitudine)
  headers = {"accept": "application/json"}
  response = requests.get(url, headers=headers)
  data = response.json()
  for item in data['data']:
    data_list.append({
        "Location ID": item['location_id'],
        "Name": item['name']
    })

for i in range(20):
  latitudine=capoluoghi[i][1]
  longitudine=capoluoghi[i][2]
  caricoArray(latitudine,longitudine)

def caricoInfo(locationId):
  url = "https://api.content.tripadvisor.com/api/v1/location/{}/details?key=4CC76D5579094823A20D1BA66DCA0BC7&language=en&currency=USD".format(locationId)
  headers = {"accept": "application/json"}
  response = requests.get(url, headers=headers)
  data = response.json()
  try:
    rating = data['rating']
  except KeyError:
    rating = 'N/A'
  data_info.append({
    "Location ID": data['location_id'],
    "Name": data['name'],
    "Rating": rating,
    "Price": data['price_level'],
    "Awards": data['awards']
  })
  return rating



for i in range(200):
  item = data_list[i]  # Ottieni l'elemento corrente
  location_id = item['Location ID']
  valutazione.append(caricoInfo(location_id))