import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Binghamton']
db = mydb["Accidents"]

year_2018 = [
    {
    "$addFields": {
      "date": { "$toDate": "$CRASH DATE" }
    }
  },
  {
    "$project": {
        "bo": "$BOROUGH",
      "year": { "$year": "$date" },
    }
  },
  {"$match":
            {
                "year": {"$in": [2018]},               
            }
    },
    {'$group':
            {
                "_id" : "$bo", "val": {"$sum":1}   
            }
    }
]

year_2022 = [
    {
    "$addFields": {
      "date": { "$toDate": "$CRASH DATE" }
    }
  },
  {
    "$project": {
        "bo": "$BOROUGH",
      "year": { "$year": "$date" }
    }
  },
  {"$match":
            {
                "year": {"$in": [2022]}      
            }
    },
    {'$group':
            {
                "_id" : "$bo", "val": {"$sum":1}   
            }
    }
]

year_2018_result = db.aggregate(year_2018)
year_2022_result = db.aggregate(year_2022)

for w in year_2018_result:
    if(w.get('_id')=="BROOKLYN"): brooklyn_2018 =(w.get('val'))
    if(w.get('_id')=="BRONX"): bronx_2018 =(w.get('val'))
    if(w.get('_id')=="MANHATTAN"):manhattan_2018 =(w.get('val'))
    if(w.get('_id')=="QUEENS"): queens_2018 =(w.get('val'))
    if(w.get('_id')=="STATEN ISLAND"): staten_island_2018 =(w.get('val'))

for w in year_2022_result:
    if(w.get('_id')=="BROOKLYN"): brooklyn_2022 =(w.get('val'))
    if(w.get('_id')=="BRONX"): bronx_2022 =(w.get('val'))
    if(w.get('_id')=="MANHATTAN"):manhattan_2022 =(w.get('val'))
    if(w.get('_id')=="QUEENS"): queens_2022 =(w.get('val'))
    if(w.get('_id')=="STATEN ISLAND"): staten_island_2022 =(w.get('val'))

print(("\nPercentage of change in Accidents of each region from 2018 to 2022.\n"))

print("Accidents in BROOKLYN has changed from ",brooklyn_2018," to ",brooklyn_2022," by ", round(((brooklyn_2022 - brooklyn_2018)/brooklyn_2018)*100,2),"%" )
print("Accidents in BRONX has changed from ",bronx_2018," to ",bronx_2022," by ", round(((bronx_2022 - bronx_2018)/bronx_2018)*100,2),"%" )
print("Accidents in MANHATTAN has changed from ",manhattan_2018," to ",manhattan_2022," by ", round(((manhattan_2022 - manhattan_2018)/manhattan_2018)*100,2),"%" )
print("Accidents in QUEENS has changed from ",queens_2018," to ",queens_2022," by ", round(((queens_2022 - queens_2018)/queens_2018)*100,2),"%" )
print("Accidents in STATEN ISLAND has changed from ",staten_island_2018," to ",staten_island_2022," by ", round(((staten_island_2022 - staten_island_2018)/staten_island_2018)*100,2),"%" )
print("\nNote: Negative sign in percentage say that there has been decrease in the Accidents")

# CODE FOR VISULAIZATION USING MATPLOTLIB 
import matplotlib.pyplot as plt
import numpy as np
# CODE FOR MULTIPLE BAR GRAPH
la = ['BROOKLYN','BRONX','MANHATTAN','QUEENS',"STATEN ISLAND"]
X_axis = np.arange(len(la))
fig,ax = plt.subplots()
ax.bar(X_axis - 0.2,[brooklyn_2018,bronx_2018,manhattan_2018,queens_2018,staten_island_2018], 0.4,label='2018')
ax.bar(X_axis + 0.2,[brooklyn_2022,bronx_2022,manhattan_2022,queens_2022,staten_island_2022], 0.4,label='2022')
plt.xticks(X_axis, la)
ax.legend()
plt.show()