from tkinter import *

import mysql.connector

class Login:

    def __init__(self):

        try:
            self.conn = mysql.connector.connect(host='localhost',user='root',password='',database='tinder')
            self.mycursor = self.conn.cursor()

        except ProgrammingError as e:
            print("Can't connect to database!!!Try again")
            self.conn = 'undefined'
            self.mycursor = 'undefined'

        self.root = Tk()
        self.root.title('Login')
        self.root.minsize(300, 400)
        self.root.maxsize(300, 400)

        self.email_label = Label(self.root, text='Email')
        self.email_label.pack()

        self.email_input = Entry(self.root)
        self.email_input.pack()

        self.password_label = Label(self.root, text='Password')
        self.password_label.pack()

        self.password_input = Entry(self.root)
        self.password_input.pack()



        self.button = Button(self.root, text='Login', command=lambda : self.check())
        self.button.pack()

        self.register_label = Label(self.root, text='Not a member')
        self.register_label.pack()

        self.register_button = Button(self.root,text='Register',command=lambda:self.register())
        self.register_button.pack()

        self.root.mainloop()

    def check(self):

        email=self.email_input.get()
        password=self.password_input.get()

        if(email=="" or password==""):
            self.root12=Tk()
            self.root12.title("Validation window")
            self.root12.minsize(300,400)
            self.root12.maxsize(300,400)

            self.root12.la=Label(self.root12,text="Please fill in!!").pack()

            self.btn12=Button(self.root12,text="OK",command=lambda:self.root12.destroy()).pack()

            self.root12.mainloop()
        else:
            self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))

            user_list=self.mycursor.fetchall()


            if len(user_list)>0:
                self.root100=Tk()
                self.root100.title('Confirmation Window')
                self.root100.minsize(300,400)
                self.root100.maxsize(300,400)
                self.msg=Label(self.root100,text='WELCOME!!!')
                self.msg.pack();

                self.btn100=Button( self.root100, text="OK",command=lambda:self.user_menu())
                self.btn100.pack()
                for i in user_list:
                    self.current_user_id=i[0]

            else:
                self.root100 = Tk()
                self.root100.title('Confirmation Window')
                self.root100.minsize(300, 400)
                self.root100.maxsize(300, 400)
                self.msg = Label(self.root100, text='INCORRECT CREDENTIALS!!!!!')
                self.msg.pack();

                self.btn100=Button(self.root100,text="OK",command=lambda:self.root100.destroy()).pack();
            self.root100.mainloop()
    def register(self):
        self.root1=Tk()
        self.root1.title('Register')
        self.root1.minsize(300,400)
        self.root1.maxsize(300,400)
        self.name_label=Label(self.root1,text='Name')
        self.name_label.pack()

        self.name_input=Entry(self.root1)
        self.name_input.pack()

        self.email1_label = Label(self.root1, text='Email')
        self.email1_label.pack()

        self.email1_input = Entry(self.root1)
        self.email1_input.pack()

        self.password1_label = Label(self.root1, text='Password')
        self.password1_label.pack()

        self.password1_input = Entry(self.root1)
        self.password1_input.pack()

        self.gender_label = Label(self.root1, text='Gender')
        self.gender_label.pack()

        self.gender_input = Entry(self.root1)
        self.gender_input.pack()

        self.age_label = Label(self.root1, text='Age')
        self.age_label.pack()

        self.age_input = Entry(self.root1)
        self.age_input.pack()

        self.city_label = Label(self.root1, text='City')
        self.city_label.pack()

        self.city_input = Entry(self.root1)
        self.city_input.pack()


        self.button1=Button(self.root1,text='Register',command=lambda : self.email_check())
        self.button1.pack()

        self.root1.mainloop()



    def my_insert(self):

        name=self.name_input.get()
        email1=self.email1_input.get()
        password1=self.password1_input.get()
        gender=self.gender_input.get()
        age=self.age_input.get()
        city=self.city_input.get()




        self.mycursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`)
              VALUES(NULL,'{}','{}','{}','{}','{}','{}')""".format(name,email1,password1,gender,age,city))

        self.conn.commit()



    def user_menu(self):
        self.root2=Tk()
        self.root2.title("User_Menu")
        self.root2.maxsize(300,400)
        self.root2.minsize(300,400)

        self.btn1=Button(self.root2,text="View All Users",command=lambda:self.view_users())
        self.btn1.pack()

        self.btn2 = Button(self.root2, text="View All Proposals",command=lambda:self.view_proposals())
        self.btn2.pack()

        self.btn3 = Button(self.root2, text="View Requests",command=lambda:self.view_requests())
        self.btn3.pack()

        self.btn4 = Button(self.root2, text="View Matches",command=lambda:self.view_matches())
        self.btn4.pack()

        self.btn5 = Button(self.root2, text="Logout",command=lambda:self.logout())
        self.btn5.pack()

        self.root2.mainloop()


    def email_check(self):

        if(self.name_input.get()=="" or self.email1_input.get()=="" or self.password1_input.get()=="" or self.gender_input.get()==""
                or self.age_input.get()=="" or self.city_input.get()==""):
                self.root99=Tk()
                self.root99.title("Validation Window")
                self.root99.minsize(300,400)
                self.root99.maxsize(300,400)


                self.l=Label(self.root99,text="Insufficient data!!").pack()
                self.btn99=Button(self.root99,text="OK",command=lambda:self.root99.destroy())
                self.btn99.pack()

                self.root99.mainloop()
        else:
                self.mycursor.execute("""SELECT `email` FROM `users` WHERE `email` LIKE '{}'""".format(self.email1_input.get()))

                a = self.mycursor.fetchall()

                counter = 0
                for i in a:
                    counter = counter + 1

                root3=Tk()
                root3.maxsize(200,200)
                root3.minsize(200,200)
                if counter > 0:
                    msgbox=Label(root3,text="Unsuccessful!!!Email already exists!!!").pack()
                    btn=Button(root3,text="OK",command=lambda:root3.destroy()).pack()


                else:
                    self.my_insert()
                    msgbox = Label(root3, text="Successful").pack()
                    btn=Button(root3,text="OK",command=lambda:root3.destroy()).pack()
                    self.root1.destroy()



                root3.mainloop()

    def view_users(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))

        all_users = self.mycursor.fetchall()
        self.root4=Tk()
        self.root4.title("All Users")
        self.root4.maxsize(1000,1000)
        self.root4.minsize(300,500)
        self.result=Label(self.root4,text="",bg='white',width=50,height=20)
        self.result.pack()
        self.btn6=Button(self.root4,text='Click Here',command=lambda:self.call_id())
        self.btn6.pack()

        for i in all_users:
            p=str(i[0])+'|'+i[1]+'|'+i[4]+'|'+str(i[5])+'|'+i[6]+'\n'
            new_text=self.result['text']+p
            self.result.configure(text=new_text)
        self.root4.mainloop()


    def call_id(self):
        self.root5=Tk()
        self.root5.title("Enter id")
        self.root5.maxsize(300,200)
        self.root5.minsize(300,200)
        self.juliet_label=Label(self.root5,text="Enter the id of the user you want to propose")
        self.juliet_label.pack()
        self.juliet_input=Entry(self.root5)
        self.juliet_input.pack()
        self.btn7=Button(self.root5,text='ok',command=lambda:self.id_check())
        self.btn7.pack()

        self.root5.mainloop()

    def id_check(self):
        romeo_id=self.current_user_id
        self.mycursor.execute("""SELECT `juliet_id` FROM `proposal` WHERE `juliet_id` LIKE '{}' AND `romeo_id` LIKE '{}'"""
                              .format(self.juliet_input.get(),romeo_id))
        o=self.mycursor.fetchall()
        counter=0
        for i in o:
            counter=counter+1
        tk=Tk()
        tk.title("Check Box")
        tk.maxsize(300,300)
        tk.minsize(300,300)
        if counter>0:
            l1=Label(tk,text="Already Sent",height=50,width=50)
            l1.pack()
        else:
            l1=Label(tk,text="Proposal sent successfully!!!Fingers crossed!!",height=50,width=50)
            l1.pack()
            self.propose(romeo_id)
        id1=Button(tk,text="ok",command=lambda:tk.destroy())
        self.root4.destroy()
        self.root5.destroy()
        id1.pack()
        tk.mainloop()

    def propose(self,romeo_id):
        self.mycursor.execute("""INSERT INTO `proposal`(`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}')"""
                              .format(romeo_id,self.juliet_input.get()))
        self.conn.commit()

    def view_proposals(self):
        self.mycursor.execute("""SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`romeo_id` LIKE '{}'""".format(self.current_user_id))

        proposed_user_list=self.mycursor.fetchall()

        self.root6=Tk()
        self.root6.title("Proposed List")
        self.root6.maxsize(1000, 1000)
        self.root6.minsize(300, 500)
        self.result1 = Label(self.root6, text="", bg='white', width=50, height=20)
        self.result1.pack()
        self.but1 = Button(self.root6, text='OK', command=lambda:self.root6.destroy())
        self.but1.pack()

        for i in proposed_user_list:
            s=i[4]+'|'+i[7]+'|'+str(i[8])+'|'+i[9]+'\n'
            new_text =self.result1['text'] + s
            self.result1.configure(text=new_text)
        self.root6.mainloop()


    def view_requests(self):
        self.mycursor.execute(
            """SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`juliet_id` LIKE '{}'""".format(
                self.current_user_id))

        requested_user_list = self.mycursor.fetchall()

        self.root7 = Tk()
        self.root7.title("Requested List")
        self.root7.maxsize(1000, 1000)
        self.root7.minsize(300, 500)
        self.result2 = Label(self.root7, text="", bg='white', width=50, height=20)
        self.result2.pack()
        self.but2 = Button(self.root7, text='OK', command=lambda: self.root7.destroy())
        self.but2.pack()

        for i in requested_user_list:
            s=i[4]+ '|'+ i[7]+ '|'+ str(i[8])+ '|'+ i[9]+"\n"
            new_text=self.result2['text'] + s
            self.result2.configure(text=new_text)
        self.root7.mainloop()


    def view_matches(self):
        self.mycursor.execute("""SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE `juliet_id` IN (SELECT `romeo_id` FROM `proposal`
                  WHERE `juliet_id` LIKE '{}') AND `romeo_id` LIKE '{}'""".format(self.current_user_id,
                                                                                  self.current_user_id))

        proposed_user_list = self.mycursor.fetchall()

        self.root8 = Tk()
        self.root8.title("Matches List")
        self.root8.maxsize(1000, 1000)
        self.root8.minsize(300, 500)
        self.result3 = Label(self.root8, text="", bg='white', width=50, height=20)
        self.result3.pack()
        self.but3 = Button(self.root8, text='OK', command=lambda: self.root8.destroy())
        self.but3.pack()

        for i in proposed_user_list:
            s=i[4]+ '|'+ i[7]+ '|'+ str(i[8])+ '|'+ i[9]+"\n"
            new_text=self.result3['text']+s
            self.result3.configure(text=new_text)
        self.root8.mainloop()

    def logout(self):
        self.current_user_id=0
        tk2=Tk()
        tk2.title("Logout")
        tk2.maxsize(200,300)
        tk2.minsize(200,300)
        label=Label(tk2,text="You are logged out!!!",bg='white',width=50,height=10)
        label.pack()
        but4=Button(tk2,text="OK",command=lambda:tk2.destroy())
        but4.pack()
        self.root2.destroy()


        tk2.mainloop()

obj1=Login()