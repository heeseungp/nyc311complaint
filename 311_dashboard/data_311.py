import pandas as pd
import json
import pprint
from pymongo import MongoClient
from flask import Flask, render_template

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
    querydata = db.complaints.find_one()
    return render_template('index.html', test= querydata['Agency'])

if __name__ == "__main__":
    app.run(port=8000, debug=True)
