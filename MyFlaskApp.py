from flask import Flask, redirect, url_for, render_template, request, session

import pandas as pd 
from numpy import mean
from numpy import std
from datetime import timedelta

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)




@app.route("/")
def home():
	print("je suis dans home")
	return render_template("home.html")

@app.route("/Set Parameters", methods=["POST", "GET"])
def set_parameters(): #set_parameters()
	if request.method == "POST":
		session.permanent = True
		loss = request.form["loss"]
		learningrtsup = request.form["learningrtsup"]
		learningrtinf = request.form["learningrtinf"]
		estimators = request.form["estimators"]
		subsamplesup = request.form["subsamplesup"]
		subsampleinf = request.form["subsampleinf"]

		session["loss"] = loss
		session["learningrtsup"] = learningrtsup
		session["learningrtinf"] = learningrtinf
		session["estimators"] = estimators
		session["subsamplesup"] = subsamplesup
		session["subsampleinf"] = subsampleinf

		return redirect(url_for("prediction"))
	else:
		if "loss" in session:
			return redirect(url_for("reset_parameters"))
		#set=open("C:/Users/alixp/Programmation/Python_Projects/Facebook_Comments_Project/contact-form-18/index.html").read()
		return render_template("set_parameters.html")

@app.route("/Prediction")
def prediction():#prediction
	if "loss" in session and "learningrtsup" in session and "learningrtinf" in session and "estimators" in session and "subsamplesup" in session and "subsampleinf" in session:
		loss = session["loss"]
		learningrtsup = session["learningrtsup"]
		learningrtinf = session["learningrtinf"]
		estimators = session["estimators"]
		subsamplesup = session["subsamplesup"]
		subsampleinf = session["subsampleinf"]

		# Load dataset
		datafb1 = pd.read_csv("Dataset/Training/Features_Variant_1.csv",index_col = None,header = None)

		# Prepare data
		column_names= ["Page Popularity/likes","Page Checkings","Page talking about","Page Category",
		"Derived_5","Derived_6","Derived_7","Derived_8","Derived_9","Derived_10","Derived_11","Derived_12","Derived_13","Derived_14",
		"Derived_15","Derived_16","Derived_17","Derived_18","Derived_19","Derived_20","Derived_21","Derived_22",
		"Derived_23","Derived_24","Derived_25","Derived_26","Derived_27","Derived_28","Derived_29",
		"CC1","CC2","CC3","CC4","CC5","Base time","Post length","Post Share Count","Post Promotion Status"
		,"H Local","Post published weekday_Sunday","Post published weekday_Monday","Post published weekday_Tuesday",
		"Post published weekday_Wednesday","Post published weekday_Thursday","Post published weekday_Friday","Post published weekday_Saturday",
		"base_dt_weekday_Sunday","base_dt_weekday_Monday","base_dt_weekday_Tuesday","base_dt_weekday_Wednesday",
		"base_dt_weekday_Thursday","base_dt_weekday_Friday","base_dt_weekday_Saturday","Target Variable"]

		datafb1.columns=column_names

		# Split the dataset
		X=datafb1[datafb1.columns.difference(['Target Variable','weekday'])]
		y=datafb1["Target Variable"]
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

		scaler = StandardScaler()
		scaler.fit(X_train)                
		X_train = scaler.transform(X_train)
		X_test  = scaler.transform(X_test)

		# fit the model on the whole dataset
		parametersboost={ "loss":[f"{loss}"], "learning_rate":[float(learningrtinf),float(learningrtsup)], "n_estimators":[int(estimators)], "subsample":[float(subsampleinf),float(subsamplesup)]}
		algoboost=GradientBoostingRegressor()
		gridboost = GridSearchCV(algoboost, parametersboost, n_jobs=-1)
		gridboost.fit(X_train, y_train)		
		print("Resultat de la prédiction : ", gridboost.best_score_, gridboost.best_estimator_)  
		result=open("templates/prediction.html").read().format(p1=loss,p2=learningrtinf,p3=learningrtsup,p4=estimators,p5=subsampleinf,p6=subsamplesup,p7=gridboost.best_score_,p8=gridboost.best_estimator_)
		return result

	else:
		print("aucun parametre dans la session")
		return redirect(url_for("set_parameters"))

	#return render_template('prediction.html')


@app.route("/Refresh Parameters", methods=["POST","GET"])
def reset_parameters():
	session.pop("loss", None)
	session.pop("learningrtsup", None)
	session.pop("learningrtinf", None)
	session.pop("estimators", None)
	session.pop("subsamplesup", None)
	session.pop("subsampleinf", None)
	return redirect(url_for("set_parameters"))




if __name__ == "__main__":
	app.run(debug=True)