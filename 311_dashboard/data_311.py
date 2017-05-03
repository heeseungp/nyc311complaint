import pandas as pd
import json
from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(port=8000, debug=True)
