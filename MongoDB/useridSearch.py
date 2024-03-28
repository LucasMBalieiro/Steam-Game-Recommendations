from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')
result = client['MiniSteam']['users'].aggregate([
    {
        '$match': {
            'user_id': 5717215
        }
    }, {
        '$lookup': {
            'from': 'recommendations', 
            'localField': 'user_id', 
            'foreignField': 'user_id', 
            'as': 'recommendations'
        }
    }
])