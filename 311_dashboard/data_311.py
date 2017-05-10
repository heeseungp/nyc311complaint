import pandas as pd
import json
import pprint
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for

client = MongoClient('localhost', 27017)
db = client['visualization311']
#collection = db['complaints']

app = Flask(__name__)

data_path = './static/data/'

#df = pd.read_csv(data_path + '311Data1.csv')
#print(df)

@app.route("/data")
def get_data():
    df = pd.read_csv(data_path + '311DataMini.csv')
    return df.to_json(orient='records')

@app.route('/')
def hello():
    return render_template('index.html')

# testing
@app.route('/query', methods=['GET', 'POST'])
def query():    
    complaintType = request.form.getlist('options')
    fromTime = request.form['from']
    toTime = request.form['to']

    mongoListparam = []

    for item in complaintType:
        mongoListparam.append({"ComplaintType":item})

    querydata = db.complaints.find_one({"CreatedDate": {"$gte":fromTime, "$lt":toTime} , "$or" : mongoListparam })
    
    return render_template('index.html', query = querydata)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
