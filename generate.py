import numpy as np
import csv
import json

def generateJson(list,filename):
    with open("json/{}.json".format(filename),"w") as json_file:
        json.dump(list,json_file)

provinces = []
with open("data/province.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        provinces.append(row)
provinces = np.array(provinces)
generateJson(provinces.tolist(),"province")

cities = []
with open("data/city.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cities.append(row)
cities = np.array(cities)
generateJson(cities.tolist(),"city")


districts = []
with open("data/district.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        districts.append(row)
districts = np.array(districts)
generateJson(districts.tolist(),"district")

sub_districts = []
with open("data/subdistrict.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        sub_districts.append(row)
sub_districts = np.array(sub_districts)
generateJson(sub_districts.tolist(),"subdistrict")

postal_code = []
with open("data/postal_code.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        postal_code.append(row)
postal_code = np.array(postal_code)
generateJson(postal_code.tolist(),"postal_code")
