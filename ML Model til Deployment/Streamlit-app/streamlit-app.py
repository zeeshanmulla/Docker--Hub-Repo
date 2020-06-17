# -*- coding: utf-8 -*-


#from flask import Flask, request
import numpy as np
import pickle
import math
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
#import flasgger
#from flasgger import Swagger
import streamlit as st

#app=Flask(__name__)
#Swagger(app)

with open('C:\\Z\\Z Workspace\\Practice\\Projects\\ML-Ops Diabetes\\docker streamlit\\model.pkl', 'rb') as model_pkl:
    rf = pickle.load(model_pkl)

 
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["GET"])
def predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    
    """Let's Authenticate the Diabetis
    This is using docstrings for specifications.
    ---
    parameters:
        - name: Pregnancies
          in: query
          type: number
          required: true
        - name: Glucose
          in: query
          type: number
          required: true
        - name: BloodPressure	
          in: query
          type: number
          required: true
        - name: SkinThickness
          in: query
          type: number
          required: true
        - name: Insulin
          in: query
          type: number
          required: true
        - name: BMI
          in: query
          type: number
          required: true
        - name: DiabetesPedigreeFunction	
          in: query
          type: number
          required: true
        - name: Age	
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
        
    """
    #Pregnancies = request.args.get('Pregnancies')
    #Glucose = request.args.get('Glucose')
    #BloodPressure = request.args.get('BloodPressure')
    #SkinThickness = request.args.get('SkinThickness')
    #Insulin = request.args.get('Insulin')
    #BMI = request.args.get('BMI')
    #DiabetesPedigreeFunction = request.args.get('DiabetesPedigreeFunction')
    #Age = request.args.get('Age')
    pred = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]).astype(np.float64)
    prediction = rf.predict(pred)
    print(prediction)
    return "result "+str(prediction)

def main():
    st.title("Diabetes Authenticator")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white; text-align:cener;"> Streamlit Diabetes Authenticator App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies", "Type Here")
    Glucose = st.text_input("Glucose", "Type Here")
    BloodPressure = st.text_input("BloodPressure", "Type Here")
    SkinThickness = st.text_input("SkinThickness", "Type Here")
    Insulin = st.text_input("Insulin", "Type Here")
    BMI = st.text_input("BMI", "Type Here")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction", "Type Here")
    Age = st.text_input("Age", "Type Here")
    result = " "
    if st.button("Predict"):
        result = predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    st.success(f'The O/P is {result}')
    if st.button("About"):
        st.text("For More About Streamlit")
        st.text("Visit 'https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83'")


if __name__=='__main__':
    main()


