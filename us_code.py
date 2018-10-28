import csv
f = open ("guns.csv", "r")
csv_reader = csv.reader (f)
data = list (csv_reader)
print (data [:5])

headers = data [0]
data = data [1:]
print (headers)
print (data [:5])

years = [row[1] for row in data]

year_counts = {}
for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else:
        year_counts[year] += 1
year_counts

import datetime
dates = [datetime.datetime(year = int (row [1]), month = int (row [2]), day = 1) for row in data]
print (dates[:5])

date_counts = {}
for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else: date_counts[date] += 1
date_counts

sexes = [row [5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 1
    else:
        sex_counts[sex] += 1
sex_counts

races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 1
    else:
        race_counts[race] += 1
race_counts

g = open ("census.csv", "r")
csv_reader1 = csv.reader (g)
census = list (csv_reader1)
census

mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk = {}
for k, v in race_counts.items():
    race_per_hundredk [k] = (v/ mapping [k])* 100000
race_per_hundredk

intents = [row [3] for row in data]
races = [row [7] for row in data]
homicide_race_counts = {}
for i, race in enumerate (races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents [i] == "Homicide":
        homicide_race_counts[race] += 1
race_per_hundredk = {}
for k, v in  homicide_race_counts.items():
    homicide_race_counts[k] = (v/ mapping[k])*100000
homicide_race_counts