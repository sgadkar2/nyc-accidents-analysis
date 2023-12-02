import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Binghamton']
db = mydb["Accidents"]

contributing_factors = [
  {
    "$project": {
        "people_killed" : { "$add" : ["$NUMBER OF PEDESTRIANS KILLED", "$NUMBER OF CYCLIST KILLED", "$NUMBER OF MOTORIST KILLED"]},
        "people_injured" : { "$add" : ["$NUMBER OF PEDESTRIANS INJURED", "$NUMBER OF CYCLIST INJURED", "$NUMBER OF MOTORIST INJURED"]},
        "co" : "$CONTRIBUTING FACTOR VEHICLE 1"
    }
  },
    {'$group':
            {
                "_id" : "$co" , "val": {"$sum":"$people_killed"} , "val1": {"$sum":"$people_injured"}
            }
    },
    {
            '$sort' : {"val": -1}
    },
    { 
        "$skip" : 1
    },
    { 
        "$limit" : 10
    }
]

people= []
reason = []
contributing_factors_ = db.aggregate(contributing_factors)
print("\nPeople_Killed    People_Injured  Contributing Factor")
for w in contributing_factors_:
    people.append(w.get("val"))
    reason.append(w.get("_id"))
    print('    ',w.get("val"),'     \t',w.get("val1"),'     \t', w.get("_id").strip())

# CODE FOR VISULAIZATION USING MATPLOTLIB 
import matplotlib.pyplot as plt

# CODE FOR PIE CHART
fig,ax = plt.subplots()
ax.set_title("Severity of top ten contributing factors")
ax.pie(people,labels=reason)
plt.show()