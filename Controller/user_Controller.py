from flask import Blueprint,request,jsonify,render_template,url_for,flash,redirect,session
import os
from Model.user_Model import Model
import pandas as pd
home_api = Blueprint('homeapi',__name__)
obj_model = Model()



@home_api.route("/",methods=['GET'])
def Home():
    if "id" not in session:
        return render_template('HomePage.html')
    else:
            return render_template("HomePage.html")   


@home_api.route("/signup",methods=["GET","POST"])
def Signup():
    if request.method == 'POST':
        user_name = request.form["Username"]
        Email = request.form["Email"]
        Password = request.form["Password"]
        check = obj_model.check_user_exists(Email,Password)
        if len(check)>0:
            return render_template('/login')
        else:
            msg = "You logged in successfully!"
            obj_model.Model_signup(user_name,Email,Password)
            return render_template("Visualization.html",msg=msg)
    else:
        return render_template("login.html")

@home_api.route("/login",methods=["GET","POST"])
def Login():
    if request.method == 'POST':
        Email = request.form["Email"]
        Password = request.form["Password"]
        # print(Email,Password,sep="\n")
        # print(obj_model.get_data(Email,Password),type(Password),type(Email))
        check = obj_model.check_user_exists(Email,Password)
        if len(check)>0:
            session["id"] = check[0]["id"]
            print("session --> ",session)
            return redirect("/Visualisation")
        else:
            return redirect('/login')
    else:
        return render_template("login.html")        

@home_api.route('/logout')
def logout():
        session.pop("id")
        return redirect('/home')


@home_api.route("/Contact",methods=["GET","POST"])
def Contact():
        if request.method == "POST":
            First_Name = request.form["firstname"]
            Last_Name  = request.form["lastname"]
            Contact    = request.form["contact_no"]
            Country    = request.form["country"]
            Subject    = request.form["subject"]
            obj_model.Model_Contact_Exists_Already(Contact)
            obj_model.Model_Contact(First_Name,Last_Name,Contact,Country,Subject) 
            return redirect("/login")
        else:
            return render_template("Contact.html")
    

@home_api.route("/About",methods=["GET"])
def About():
    return render_template("About.html")


@home_api.route("/Visualisation",methods=["GET","POST"])
def visualize():
    if "id" in session:
        if request.method == "POST":
            file = request.files["file"]
            if file:
                df = pd.read_csv(file)
                print(df)
            return redirect("/Uploader")
        else:
            return render_template("Visualization.html")

@home_api.route("/Uploader",methods=["GET","POST"])
def uploader():
    if "id" in session:
        if request.method == "POST":
            pass
        else:
            return render_template("upload.html")
    else:
        return redirect("/login")






