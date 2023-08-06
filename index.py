from flask import Flask,render_template,redirect,url_for

from tkinter import *
from PIL import ImageTk

app = Flask(__name__)


@app.route('/')
def landpage():
    return render_template('index.html')

@app.route('/')
#Functuionality Part
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='Closed12.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='open12.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



#Login_window part
#create obtect
Login_window=Tk()
Login_window.title("LogIn/Reg Page")
#add image file
#----bgImage=ImageTk.PhotoImage(file='Sharing-Square.jpg')
#creating label to show image
#---bgLabel=Label(Login_window, image=bgImage)
#---bgLabel.place(x = 0, y = 0)

# set window size
Login_window.geometry("1800x1800")

#set window color
Login_window.configure(bg='green')




# window size to the bg image size
#---Login_window.geometry("1800x1800")


#adding a heading
heading=Label(Login_window,text='USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold'),bg='green',fg='firebrick1')
heading.pack(pady = 50)

#entry fields

usernameEntry=Entry(Login_window,width=30, font=('Microsoft Yahei UI Light',14,'bold'),
                    bd=0,fg='black',bg='green')
usernameEntry.place(x=673, y=155)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
Frame(Login_window,width=363,height=3,bg='firebrick1').place(x=672, y=180)

#password entries
passwordEntry=Entry(Login_window,width=30, font=('Microsoft Yahei UI Light',14,'bold'),
                    bd=0,fg='black',bg='green')
passwordEntry.place(x=673, y=230)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)
Frame(Login_window,width=363,height=3,bg='firebrick1').place(x=672, y=255)

openeye=PhotoImage(file='open12.png')
eyeButton=Button(Login_window,image=openeye,bd=0,bg='green',activebackground='green',
                 cursor='hand2',command=hide)
eyeButton.place(x=1004,y=210)



forgetButton=Button(Login_window,text='Forgot Password',bd=0,bg='green',activebackground='green',
                 cursor='hand2',activeforeground='white')
forgetButton.place(x=943,y=260)

loginButton=Button(Login_window,text='Login',font=('Open Sans',17,'bold'),
                   fg='white',bg='firebrick1',activebackground='white',activeforeground='black',cursor='hand2',
                   bd=0,width=25)
loginButton.place(x=672,y=330)


orLabel=Label(Login_window,text='---------------- OR ----------------',
              font=('Open Sans',20), fg='black',bg='green')
orLabel.place(x=672,y=430)

FacebookLogo=PhotoImage(file='facebook.png')
fbLabel=Label(Login_window,image=FacebookLogo,bg='green')
fbLabel.place(x=740, y=490)

TwitterLogo=PhotoImage(file='twitter.png')
TwitterLabel=Label(Login_window,image=TwitterLogo,bg='green')
TwitterLabel.place(x=820, y=490)

GoogleLogo=PhotoImage(file='google.png')
GoogleLabel=Label(Login_window,image=GoogleLogo,bg='green')
GoogleLabel.place(x=900, y=490)

signupLabel=Label(Login_window,text='Dont have an account?',
              font=('Open Sans',12,'bold'), fg='firebrick1',bg='green')
signupLabel.place(x=672,y=580)

newaccountButton=Button(Login_window,text='create an account',font=('Open Sans',12,'bold underline'),
                   fg='blue',bg='green',activebackground='blue',activeforeground='black',cursor='hand2',
                   bd=0)
newaccountButton.place(x=870,y=580)


Login_window.mainloop() 

if __name__ == "__main__":
    app.run()



