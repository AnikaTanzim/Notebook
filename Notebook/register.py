from tkinter import *
import os


def delete3():
    screen3.destroy()
    session()
    
def delete4():
    screen4.destroy()
    
def delete5():
    screen5.destroy()
    
def delete10():
    screen10.destroy()

def saved():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("info")
    screen10.geometry("200x150")
    Label(screen10,text="").pack()
    Label(screen10,text="").pack()
    Label(screen10, text = "Your note is saved",fg = "green", font=("calibri",13)).pack()
    Label(screen10,text="").pack()
    Button(screen10, text ="OK", command=delete10).pack()
    
def save():
    filename =raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, 'w')
    data.write(notes)
    data.close()

    saved()

    
def create_note():
    screen7 = Toplevel(screen)
    screen7.title("info")
    screen7.geometry("600x500")
        
    global raw_filename 
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()

    Label(screen7,text="please enter a filename for the note below : ").pack()
    Entry(screen7, textvariable = raw_filename).pack()
    Label(screen7,text="please enter the notes for the file below : ").pack()
    Entry(screen7, textvariable = raw_notes).pack()
    Button(screen7, text = "Save",command=save).pack()

def view():
    screen11 = Toplevel(screen)
    screen11.title("file view")
    screen11.geometry("600x500")

    filename1 =raw_filename1.get()
    data= open(filename1,'r')
    data1 = data.read()
    Label(screen11,text=data1).pack()
  
def view_note():
    screen8 = Toplevel(screen)
    screen8.title("info")
    screen8.geometry("800x500")
    Label(screen8,text = "please use one of these notes").pack()
    
    all_files = os.listdir()
    for x in all_files:
        Label(screen8,text = x).pack()
    
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen8, textvariable = raw_filename1).pack()
    Button(screen8, text = "View",command=view).pack()

def delete():
    screen13 = Toplevel(screen)
    screen13.title("info")
    screen13.geometry("200x150")

    filename3 =raw_filename2.get()
    os.remove(filename3)
    Label(screen13,text=filename3+ "is removed").pack()
    
def delete_note():
    screen9 = Toplevel(screen)
    screen9.title("dashboard")
    screen9.geometry("600x500")
    Label(screen9,text = "please use one of these notes").pack()
    
    all_files = os.listdir()
    for x in all_files:
        Label(screen9,text = x).pack()
    
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen9, textvariable = raw_filename2).pack()
    Button(screen9, text = "Delete",command=delete).pack()


def session():
    screen6 = Toplevel(screen)
    screen6.title("dashboard")
    screen6.geometry("600x500")
    Label(screen6,text="Welcometo the dashboard").pack()
    Button(screen6,text ="Create Note", command=create_note).pack()
    Button(screen6,text ="View Note", command=view_note).pack()
    Button(screen6,text ="Delete Note", command=delete_note).pack()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("200x150")
    Label(screen3,text="").pack()
    Label(screen3,text="").pack()
    Label(screen3, text = "login succesful",fg = "green", font=("calibri",13)).pack()
    Label(screen3,text="").pack()
    Button(screen3,text ="OK", command=delete3).pack()
    

    
def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Login")
    screen4.geometry("200x150")
    Label(screen4,text="").pack()
    Label(screen4,text="").pack()
    Label(screen4, text = "password has not been recognized",fg = "red", font=("calibri",13)).pack()
    Label(screen4,text="").pack()
    Button(screen4,text ="OK", command=delete4).pack()

    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Login")
    screen5.geometry("200x150")
    Label(screen5,text="").pack()
    Label(screen5,text="").pack()
    Label(screen5, text = "user not found",fg = "red", font=("calibri",13)).pack()
    Label(screen5,text="").pack()
    Button(screen5, text ="OK", command=delete5).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    
    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()

    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)

    Label(screen1, text = "registration succesful",fg = "green", font=("calibri",13)).pack()
    

def login_verify():
    username_info1 = usernameVerify.get()
    password_info1 = passwordVerify.get()
    usernameEntry1.delete(0,END)
    passwordEntry1.delete(0,END)
    list_of_files= os.listdir()
    
    list1=[]
    if username_info1 in list_of_files:
        file1 = open(username_info1, 'r') 
        Lines = file1.readlines()

        for line in Lines:
            list1.append(line.strip())
        print(list1)
        
        if password_info1 == list1[1]:
            login_success()             
        else:
            password_not_recognized() 
    else:
        user_not_found()
        
    


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x300")

    global username
    global password
    global usernameEntry
    global passwordEntry
    
    username= StringVar()
    password= StringVar()
    
    Label(screen1,text="please enter details below").pack()
    Label(screen1,text="").pack()
    
    Label(screen1,text="Username *").pack()
    usernameEntry= Entry(screen1,textvariable = username)
    usernameEntry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Password *").pack()
    passwordEntry= Entry(screen1,textvariable = password)
    passwordEntry.pack()
    Label(screen1,text="").pack()
    Button(screen1, text = "Register", width = 10, height=2, command=register_user).pack()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x300")
    
    Label(screen2,text="please enter details below to login").pack()
    Label(screen2,text="").pack()

    global usernameVerify
    global passwordVerify
    
    usernameVerify = StringVar()
    passwordVerify = StringVar()

    global usernameEntry1
    global passwordEntry1
    
    Label(screen2,text="Username *").pack()
    usernameEntry1= Entry(screen2,textvariable = usernameVerify)
    usernameEntry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password *").pack()
    passwordEntry1= Entry(screen2,textvariable = passwordVerify)
    passwordEntry1.pack()
    Label(screen2,text="").pack()
    Button(screen2, text = "Login", width = 10, height=2, command=login_verify).pack()
    

    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x300")
    screen.title("Register Book")
    Label(text = " Register Book", bg = "grey",width="500",height="3" ,font=("Calibri",13)).pack()
    #Label(text = " Register here!", bg = "grey",width="500",height="3" ,font=("Calibri",12)).pack()
    Label(text="").pack()
    Button(text = "Login",width="30",height="3", command=login).pack()
    Label(text="").pack()
    Button(text = "Register",width="30",height="3", command= register).pack()

    screen.mainloop()
main_screen()
