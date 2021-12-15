from flask import Flask,jsonify, render_template, request, redirect,url_for,escape
import json


app = Flask(__name__)
jData = json.loads(open('./cars.json').read())
data=jData["Cars"]

@app.route('/')
def car_main():
    return render_template("index.html")

@app.route('/carsdatastorage/')
def getAllCars():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/carsdatastorage/<string:Year>/')
def getyear(Year=''):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)


@app.route('/carsdatastorage/<string:Year>/<string:ID>')
def getbrand(Year, ID):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            if element ["ID"] == ID:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/carsdatastorage/<string:Year>/<string:ID>/<string:Throttle>')
def getThrottle(Year,Throttle,ID):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            if element ["ID"] == ID:
                if element ['Throttle'] == Throttle:
                    myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')