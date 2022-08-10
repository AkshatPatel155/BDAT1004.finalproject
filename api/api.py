from unittest import result
from xml.dom.minidom import Document
import sqlconnection;
from flask import Flask, request, jsonify;
from pymongo import MongoClient;

import json


app = Flask(__name__)

@app.route("/data", methods=['POST', 'GET'])

def total_count():
    if request.method == 'GET':
            data = sqlconnection.connection()
            
            return  {"result": data.count_documents({})}


@app.route("/data/<id>",methods = ['POST','GET'])
def data_by_id(id):
    try:
        if request.method == "GET":
            data = sqlconnection.connection()
            data_by_id = data.find_one({"show_id":id})
            return {
                'show_id':data_by_id['show_id'],
                'type':data_by_id['type'],
                'title':data_by_id['title'],
                'director':data_by_id['director'],
                'cast':data_by_id['cast'],
                'country':data_by_id['country'],
                'date_added':data_by_id['date_added'],
                'release_year':data_by_id['release_year'],
                'rating':data_by_id['rating'],
                'duration':data_by_id['duration'],
                'listed_in':data_by_id['listed_in'],
                'description':data_by_id['description'],
            }
    except:
        print("An exception occured")
    
@app.route("/data/all",methods = ['POST','GET'])
def data_all():
     if request.method == "GET":
        data = sqlconnection.connection()
        for x in data.find():
            print(x)
        return jsonify({'result':[x for x in data.find()]})
    
@app.route("/data/find_by_type")
def find_by_type():
    data = sqlconnection.connection()

    return{"movie":data.count_documents({'type':"Movie"}),"tv show":data.count_documents({'type':'TV Show'})}

@app.route("/data/find_by_rating")
def find_by_rating():
    data = sqlconnection.connection()

    return{"TV-MA":data.count_documents({'rating':"TV-MA"}),"TV-14":data.count_documents({'rating':'TV-14'}),
            "NR":data.count_documents({'rating':"NR"}),"PG":data.count_documents({'rating':'PG'}),
            "R":data.count_documents({'rating':"R"}),"PG-13":data.count_documents({'rating':'PG-13'}),
            "TV-Y":data.count_documents({'rating':"TV-Y"}),"TV-G":data.count_documents({'rating':'TV-G'}),
            "TV-Y7":data.count_documents({'rating':"TV-Y7"}),"G":data.count_documents({'rating':'G'}),
            "TV-Y7-FV":data.count_documents({'rating':"TV-Y7-FV"}),"NC-17":data.count_documents({'rating':'NC-17'}),
            "UR":data.count_documents({'rating':'UR'})
            }

if __name__ == '__main__':
    app.debug = True

    app.run()

