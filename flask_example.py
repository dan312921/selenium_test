import flask
from flask import Flask
import pandas as pd
import os
app = Flask(__name__)

#http://127.0.0.1:5000/register/dan/dan
#register/<email>/<pw>

@app.route("/register/<email>/<password>")

def register(email, password):

    # Validation
    if email == "":
        return "Fail: Email must not be empty"
    if password == "":
        return "Fail: Password must not be empty"

    # Actual
    if os.path.exists("user.csv"):

        df = pd.read_csv("user.csv")
        if (df['email'] == email).sum() > 0:
            return "Fail: email exist"
        else:
            df.append([
                {"email": email, "password": password}
            ]).to_csv("user.csv", index=False)
            return "Success"

    else:
        df = pd.DataFrame(
            [[email, password]],
            columns=["email", "password"]
        )
        df.to_csv("user.csv", index=False)

        return "Success"

@app.route("/get_display_name/<email>")
def get_display_name(email):
     df=pd.read_csv("user.csv")

     if (df["email"]==email).sum()==0:
         return "fail"

     return df[df["email"]==email].iloc[0,2]

@app.route("/login/<email>/<pw>")
def login(email,pw):
    df=pd.read_csv("user.csv")
    if (df["email"] == email).sum() == 0:
        return "fail"
    if df[df["email"]==email].iloc[0,1]!=pw:
         return "wrong pw"

    resp=flask.Response("OK")
    resp.set_cookie("receipt",email)
    return resp
