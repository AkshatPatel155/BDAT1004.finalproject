from pymongo import MongoClient;

def connection():
    client = MongoClient("mongodb+srv://BDAT1004:admin@cluster0.pqjifkd.mongodb.net/?retryWrites=true&w=majority")
    db = client.get_database('BDAT1004')
    data = db.Netflix_titles

    return data

        
        