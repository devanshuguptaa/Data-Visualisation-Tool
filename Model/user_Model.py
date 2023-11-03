import mysql.connector as connection
import json
from flask import jsonify,make_response
class Model:
    def __init__(self):
        try:
            self.conn = connection.connect(host="localhost", database="website", user="root", passwd="Example@2023#",
                                        use_pure=True)
            self.curr = self.conn.cursor(dictionary=True)
            pass
        except:
            print("Some Error")
    def Model_visulaize(self):
        fig = plt.figure()

        # Add a plot to the figure
        plt.plot([1, 2, 3, 4, 5])

        # Save the figure as a PNG image
        fig.savefig('my_image.png')

        import os.path
        directory = 'D:\Start Project Website with Login and Registration\Start Project Website with Login and Registration\backend\templates'
        filename = "my_image.png"
        file_path = os.path.join(directory, filename)
        with open(file_path,"r") as f:
            print(f.read())
        return 1

    def Model_signup(self,user_name,Email,Password):
        self.curr.execute("create table if not exists Register(id int primary key auto_increment,Username varchar(255),Email varchar(255),Password varchar(255) );")
        self.conn.commit()
        self.curr.execute("insert into website.Register(Username,Email,Password) value('{}','{}','{}')".format(user_name,Email,Password))
        self.conn.commit()
        return make_response({"message":"user created Successfully"},200)
    def get_data(self,Email,Password):
        self.curr.execute("select * from Register")
        res = self.curr.fetchall()
        return res
    def check_user_exists(self,email,password):
        self.curr.execute("SELECT * FROM Register where Email like '{}'".format(email,password))
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




        


