from flask import Blueprint,request,jsonify,render_template,url_for,flash,redirect,session
import os
from werkzeug.utils import secure_filename
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
        Email     = request.form["Email"]
        Password  = request.form["Password"]
        check = obj_model.check_user_exists(Email,Password)
        if len(check)>0:
            return redirect('/login')
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
            my_dict = {'a': 1, 'b': 2} 
            # print("file: ",file,"session['file']--->",d["file"],d)
            if file:
                df = pd.read_csv(file)
                l = obj_model.get_column(df)
                row = list(df.values)
                global d 
                d = {"file":df}
            return render_template("upload.html",l=l,row=row)
        else:
            return render_template("Visualization.html")
    else:
        return redirect("/login")
            

@home_api.route("/Uploader",methods=["GET","POST"])
def uploader():
    if "id" in session:
        if request.method == "POST": 
            col1 = request.form["column1"] 
            col2 = request.form["column2"]
            file = d["file"]
            print(col1,col2)
            # print(file)
            img_path = obj_model.show_fig(col1,col2,file)
            return render_template("show_image.html",col1=col1,col2=col2,img_path = img_path)  
    else:
        return redirect("/login")

@home_api.route("/show_image",methods=["GET","POST"])
def show_image():
    if "id" in session:
            return "<h1>Finally Completed!</h1>"
    else:
        return redirect("/login")








