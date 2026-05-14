import joblib
from preprocess import preprocess 
from flask import Flask,request,jsonify
model=joblib.load('model.joblib')
vectorizer =  joblib.load('tf_idf.joblib')
