import pandas as pd
import json
import pprint
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, jsonify
from bson.json_util import dumps

client = MongoClient('localhost', 27017)
db = client['visualization311']
#collection = db['complaints']

app = Flask(__name__)

data_path = './static/data/'

#df = pd.read_csv(data_path + '311Data1.csv')
#print(df)

# @app.route("/data")
# def data():
#     df = pd.read_csv(data_path + '311DataMini.csv')
#     return df.to_json(orient='records')

#Prototype before merging
#make sure you edit index.html for url_for to /data

@app.route('/zipcode_data', methods=['GET', 'POST'])
def zipcode_data():
    zipcode_data = request.args.get('zipcode')
    # zip = request.json['zipcode']
    querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : [{"ComplaintType":"Blocked Driveway"}] })
    return dumps(querydata)


@app.route('/data', methods=['POST'])
def data():
    if (request.method == 'POST'):
        complaintType = request.form.getlist('options')
        fromTime = request.form['from']
        toTime = request.form['to']

        mongoListparam = []

        for item in complaintType:
            mongoListparam.append({"ComplaintType":item})

        querydata = db.complaints.find({"CreatedDate": {"$gte":fromTime, "$lt":toTime} , "$or" : mongoListparam })

        # result = []
        #
        # for post in querydata:
        #     result.append(post)

        return dumps(querydata)
    else:
        querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : [{"ComplaintType":"Blocked Driveway", "ComplaintType":"Rodent"}] })
        return dumps(querydata)

#    return render_template('index.html', query=querydata)

@app.route('/')
def hello():
#    querydata = db.complaints.find({"CreatedDate": {"$gte":fromTime, "$lt":toTime} , "$or" : mongoListparam })
    # querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : {"ComplaintType":"Blocked Driveway", "ComplaintType":"Rodent"} })
    # return dumps(querydata)
    return render_template('index.html')

# @app.route('/query', methods=['GET', 'POST'])
# def query():
#     complaintType = request.form.getlist('options')
#     fromTime = request.form['from']
#     toTime = request.form['to']
#
#     mongoListparam = []
#
#     for item in complaintType:
#         mongoListparam.append({"ComplaintType":item})
#
#     querydata = db.complaints.find({"CreatedDate": {"$gte":fromTime, "$lt":toTime} , "$or" : mongoListparam })
#
#     return render_template('index.html', query = type(querydata))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
