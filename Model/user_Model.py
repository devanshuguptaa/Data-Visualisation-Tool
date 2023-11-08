import mysql.connector as connection
import json
import os
from flask import jsonify,make_response
import matplotlib.pyplot as plt
import random
import pandas as pd

# class Plot:
#     def __init__(self,df,column1,column2):
#         self.df = df
#         self.column1 = column1
#         self.column2 = column2
    
#     def scatterPlot():
#         pass

#     def plot():
#         pass     

class Model:
    def __init__(self):
        try:
            self.conn = connection.connect(host="localhost", database="website", user="root", passwd="Example@2023#",
                                        use_pure=True)
            self.curr = self.conn.cursor(dictionary=True)
        except:
            print("Some Error")

    def Model_signup(self,user_name,Email,Password):
        self.curr.execute("create table if not exists Register(id int primary key auto_increment,Username varchar(255),Email varchar(255),Password varchar(255) );")
        self.conn.commit()
        self.curr.execute("insert into website.Register(Username,Email,Password) value('{}','{}','{}')".format(user_name,Email,Password))
        self.conn.commit()
        self.curr.execute("SELECT * FROM Register where Email like '{}' and Password like '{}'".format(Email,Password))
        res = self.curr.fetchall()
        return res


    def get_data(self,Email,Password):
        self.curr.execute("select * from Register")
        res = self.curr.fetchall()
        return res
        
        
    def check_user_exists(self,email,password):
        self.curr.execute("SELECT * FROM Register where Email like '{}' and Password like '{}'".format(email,password))
        res = self.curr.fetchall()
        print(res)
        return res 
    

    def check_user_exists_signup(self,email):
        self.curr.execute("SELECT * FROM Register where Email like '{}'".format(email))
        res = self.curr.fetchall()
        print(res)
        return res

    def Model_Contact(self,First_Name,Last_Name,Contact,Country,Subject):
        self.curr.execute(f"insert into website.contact values('{First_Name}','{Last_Name}',{Contact},'{Country}','{Subject}')")
        self.conn.commit()
        return make_response({"message":"user created Successfully"},200)


    def Model_Contact_Exists_Already(self,Contact):
        self.curr.execute(f"select * from contact where Contact = {Contact}")
        res = self.curr.fetchall()
        print(res)
        return res

    def get_column(self,df):
        # l = []
        # for i in df.columns.values.tolist():
        #     if df[i].dtype.kind in 'biufc':
        l = df.columns.values.tolist()
        return l




    def show_fig(self,column1,column2,df):
        try:
            fig, ax = plt.subplots()
            ax.plot(column1, column2,data=df)
            tittle = "{} v/s {}".format(column1,column2)
            plt.title(tittle)
            n = random.randint(1,1000000)
            image_name = "image" + "{}".format(n) + ".png" 
            image_path = "static\images"+"\_"+image_name
            fig.savefig(image_path)
            print(image_path)
        except:
            image_path="https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png"
        return image_path


        
















   



    # def pieplot(column1,column2,df):
    #     pyplot.pie(slice,
    #     labels =column1,
    #     colors =column2,
    #     startangle = 90,
    #     shadow = True,
    #     explode =(0,0.1,0,0,0),
    #     autopct ='%1.1f%%')
    #     pyplot.title('Training Subjects')
        
        
    







        


