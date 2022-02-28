from django.shortcuts import render, redirect
from.models import contact
from.forms import ContactForm

# data processing, CSV file (e.g. pd.read_csv)
import pandas as pd
# linear algebra
import numpy as np
import datetime

# re = regular expression
import re

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn import metrics

# ML model
from sklearn.ensemble import RandomForestClassifier


# Create your views here.
def home(request):
    if request.method == 'POST':
        input_name = request.POST.get("name1")
        input_email = request.POST.get("email1")
        input_message = request.POST.get("message1")

        contact_info = contact(name=input_name, email=input_email, message=input_message)
        contact_info.save()
    return render(request, 'weather_app/home.html')


# -------------------------------------
#  Weather Prediction Starts from here
# -------------------------------------
def weather_prediction(request):
    return render(request, 'weather_app/weather.html')

def weather_result(request):
    # loading the dataset to pandas DataFrame
    weather_dataset = pd.read_csv(r'weather_app/dataset/seattle-weather.csv')

    #convert the data type into datetime
    weather_dataset['date'] = pd.to_datetime(weather_dataset['date'])
    weather_dataset['date'] = weather_dataset['date'].values.astype(float)

    # convert categorical values to numerical values using Label Encoding
    # Label Encoding
    encoder = LabelEncoder()

    # convert categorical columns to numerical values
    weather_dataset['weather'] = encoder.fit_transform(weather_dataset['weather'])
    #After label Encoding,  Weather: Drizzle = 0,  Fog = 1, Rain = 2,  Snow = 3, Sun = 4;

    # Splitting the data set
    X = weather_dataset.drop(['weather'], axis=1)
    Y = weather_dataset['weather']

    # Splitting the data into Training data & Testing Data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Random Forest
    Classifier_random_forest=RandomForestClassifier()
    Classifier_random_forest.fit(X_train, Y_train)

    var1 = (request.GET['date'])
    var1_day = float(pd.to_datetime(var1, format="%Y-%m-%dT").day)
    # var1_month = float(pd.to_datetime(var1, format="%Y-%m-%dT").month)
    var2 = float(request.GET['precipitation'])
    var3 = float(request.GET['temp_max'])
    var4 = float(request.GET['temp_min'])
    var5 = float(request.GET['wind'])

    prediction = Classifier_random_forest.predict(np.array([var1_day,  var2, var3, var4, var5]).reshape(1, -1))
    
    predict = round(prediction[0])

    if prediction == [0]:
        # Weather = "Drizzle"
        return render(request, 'weather_app/drizzle.html')

    elif prediction == [1]:
        # Weather = "Fog"
        return render(request, 'weather_app/foggy.html')

    elif prediction == [2]:
        # Weather = "Rain"
        return render(request, 'weather_app/rainy.html')

    elif prediction == [3]:
        # Weather = "Snow"
        return render(request, 'weather_app/snow.html')
        
    else:
        # Weather = "Sun"
        return render(request, 'weather_app/sunny.html')

    return render(request, 'weather_app/weather.html')

# -------------------------------------
#  Weather Prediction end here
# -------------------------------------

# About Us start
def about(request):
    return render(request, 'weather_app/about.html')
# About Us End
