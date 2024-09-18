import pandas as pd
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hey... Welcome to my Python Program"

@app.route('/property')
def property_lst():
    df = pd.read_csv('Melbourne_housing_FULL.csv')
    return list(df.columns)

@app.route('/details/<string:suburb>/<int:min_price>/<int:max_price>', methods=['GET', 'POST'])
def specific_property(suburb=None, min_price=None, max_price=None):
    suburb = request.form.get(suburb)
    min_price = request.form.get(min_price)
    max_price = request.form.get(max_price)
    filterd_df = pd.read_csv('Melbourne_housing_FULL.csv')
    
    if suburb:
        filterd_df = filterd_df[filterd_df['Suburb'] == suburb]
    if min_price:
        filterd_df = filterd_df[filterd_df['Price'] >= min_price]
    if max_price:
        filterd_df = filterd_df[filterd_df['Price'] <= max_price] 
        
    return filterd_df.values.tolist()

if __name__ == '__main__':
    app.run(debug=True)