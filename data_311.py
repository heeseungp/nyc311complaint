# import json
# import pprint
# from pymongo import MongoClient

from flask import Flask, render_template, request, url_for, jsonify
from bson.json_util import dumps

# client = MongoClient('localhost', 27017)
# db = client['visualization311']

app = Flask(__name__)

# data_path = './static/data/'


# old one 
# @app.route("/data")
# def data():
#     df = pd.read_csv(data_path + '311DataMini.csv')
#     return df.to_json(orient='records')

#Prototype before merging
#make sure you edit index.html for url_for to /data


# @app.route('/population_data', methods=['GET', 'POST'])
# def population_data():
#     start_year = request.args.get('start_year')
#     end_year = request.args.get('end_year')
#     print('PYTHON YEARS')
#     print(start_year)
#     print(end_year)
#     population = db.population.find()
#     # querydata = db.complaints.find({"CreatedDate": {"$gte":"2010-01-00 00:00:00", "$lt":"2010-12-00 00:00:00"}})
#     querydata = db.complaints.aggregate([
#         {'$match':
#             {
#             'CreatedDate':
#                 {
#                     "$gte": start_year, "$lt":end_year
#                 }
#             }
#         },
#         { '$group':
#             { '_id': {'ZipCode': '$ZipCode'},
#                 'Density': {'$sum': 1}
#             }
#         }
#     ])
#     list = []
#     list.append(population)
#     list.append(querydata)
#     # querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : [{"ComplaintType":"Blocked Driveway", "ComplaintType":"Rodent"}] })
#     return dumps(list)


# @app.route('/zipcode_data', methods=['GET', 'POST'])
# def zipcode_data():
#     zipcode_data = request.args.get('zipcode')
#     start_month = request.args.get('start_month')
#     end_month = request.args.get('end_month')
#     # zip = request.json['zipcode']
#     querydata = db.complaints.find({"CreatedDate": {"$gte":start_month, "$lt":end_month}, "$and" : [{"ZipCode": int(zipcode_data)}]})
#     # querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : [{"ComplaintType":"Blocked Driveway", "ComplaintType":"Rodent"}] })
#     return dumps(querydata)


# @app.route('/data', methods=['POST'])
# def data():
#     if (request.method == 'POST'):
#         complaintType = request.form.getlist('options')
#         fromTime = request.form['from']
#         toTime = request.form['to']

#         mongoListparam = []

#         for item in complaintType:
#             mongoListparam.append({"ComplaintType":item})

#         querydata = db.complaints.find({"CreatedDate": {"$gte":fromTime, "$lt":toTime} , "$or" : mongoListparam })

#         return dumps(querydata)
#     else:
#         querydata = db.complaints.find({"CreatedDate": {"$gte":"2011-09-00 00:00:00", "$lt":"2011-10-00 00:00:00"} , "$or" : [{"ComplaintType":"Blocked Driveway", "ComplaintType":"Rodent"}] })
#         return dumps(querydata)

@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)