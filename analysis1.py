import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['Binghamton']
db = mydb["Accidents"]

def analy(mn,hr):
  query = [
        {
    "$addFields": {
      "date": { "$toDate": "$CRASH DATE" }
    }
  },
  {
    "$project": {
        "bo": "$BOROUGH",
      "year": { "$year": "$date" },
      "month": { "$month": "$date"},
      "hour": { "$toInt": { "$arrayElemAt": [ { "$split": [ "$CRASH TIME", ":" ] }, 0 ] } }
    }
  },
  {"$match":
            {
                "month": {"$in": mn},
                "hour": { "$in": hr }
                
            }
    },
    {'$group':
            {
                "_id" : "$bo", "val": {"$sum":1}   
            }
    },
    {
            '$sort' : {"val": -1}
    }
    ]

  query_ = db.aggregate(query)

  for w in query_:
    if(w.get('_id')=="BROOKLYN"): wd1 =(w.get('val'))
    if(w.get('_id')=="BRONX"): wd2 =(w.get('val'))
    if(w.get('_id')=="MANHATTAN"):wd3 =(w.get('val'))
    if(w.get('_id')=="QUEENS"): wd4 =(w.get('val'))
    if(w.get('_id')=="STATEN ISLAND"): wd5 =(w.get('val'))

  print('{:02d}'.format(hr[0])," -  ",'{:02d}'.format(hr[7]+1), "\t",wd1, "\t  ",wd2,"    ",wd3," \t",wd4," \t",wd5)

hr1 = [[4,5,6,7,8,9,10,11], [12,13,14,15,16,17,18,19], [20,21,22,23,0,1,2,3]]

mn1 = [12,1,2]
mn2 = [3,4,5]
mn3 = [6,7,8]
mn4 = [9,10,11]

print('Crashes happening in Winter')
print("   Time        BROOKLYN    BRONX    MANHATTAN    QUEENS     STATEN ISLAND")
for i in hr1:
  analy(mn1,i)
  
print('\nCrashes happening in Spring')
print("   Time        BROOKLYN    BRONX    MANHATTAN    QUEENS     STATEN ISLAND")
for i in hr1:
  analy(mn2,i)

print('\nCrashes happening in Summer')
print("   Time        BROOKLYN    BRONX    MANHATTAN    QUEENS     STATEN ISLAND")
for i in hr1:
  analy(mn3,i)

print('\nCrashes happening in Fall')
print("   Time        BROOKLYN    BRONX    MANHATTAN    QUEENS     STATEN ISLAND")
for i in hr1:
  analy(mn4,i)
