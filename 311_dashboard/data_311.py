import pandas as pd
import json
from flask import Flask, render_template
app = Flask(__name__)

data_path = './static/data/'

#df = pd.read_csv(data_path + '311Data1.csv')
#print(df)

winners = [
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'V.S. Naipaul', 'category':'Literature'},
    {'name': 'Dorothy Hodgkin', 'category':'Chemistry'}
]

@app.route("/data")
def get_data():
    df = pd.read_csv(data_path + '311Data2.csv')
    return df.to_json(orient='records')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
