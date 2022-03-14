import webbrowser
import tkinter as tk
from tkinter.messagebox import *
import whois,pyshorteners

#defining functions
def check_file(url):
    try:
        with open('url.txt','r') as file:
            taken_domains = file.readlines()
            if f'{url}\n' in taken_domains:
                return False
            else:
                return True
    except Exception as e:
        return True

def domaincheck():
    global url
    url = url_entry.get()
    if url == '':
        showerror('Invalid',' Please Enter A URL')
        url_entry.delete(0,tk.END)
        return
    try:
        response=whois.whois(url)
        for x in response.domain_name:
            showerror('Taken',f"{url} is taken")
            break
    except whois.parser.PywhoisError:
        if check_file(url):
            ans=askyesno('Available',f"{url} is available.\nWould you like to register this domain?")
            if ans:
                write_to_file(url)
        else:
            showerror('Taken',f"{url} is taken")
    url_entry.delete(0,tk.END)
    
def write_to_file(url):
    with open('url.txt','a') as file:
        file.write(url+'\n')

def domaincheckmain():
    global url_entry
    #creating root window
    root = tk.Tk()
    root.title('Url Tool')
    root.geometry('400x300')

    title_label = tk.Label(root,text='ENTER DOMAIN BELOW',font=('Cabin Sketch',18))
    title_label.place(relx=0.5,rely=0.25,anchor='center')

    url_entry = tk.Entry(root,font=('Cabin Sketch',15))
    url_entry.place(relx=0.5,rely=0.5,anchor='center')
    btnRead=tk.Button(root, height=1, width=10, bd=4,bg='white',text="Check", command=domaincheck)
    btnRead.place(relx=0.5,rely=0.7,anchor='center')
    root.mainloop()

def shorten():
    url = web_entry1.get()
    if url == '':
        showerror('Invalid',' Please Enter A URL')
        web_entry1.delete(0,tk.END)
        return
    try:
        url = web_entry1.get()
        maker=pyshorteners.Shortener()
        short_url=maker.tinyurl.short(url)
        web_entry1.delete(0,tk.END)
        web_entry1.insert(tk.END,short_url)
        root=tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(short_url)
        showinfo(title='Information', message='Link Copied!')
        root.destroy()
    
    except Exception as e:
        print()
    

def linkshortenermain():
    global web_entry1
    #creating root window
    root = tk.Tk()
    root.title('Shortener Tool')
    root.geometry('400x300')

    title_label = tk.Label(root,text='ENTER URL TO SHORTEN',font=('Cabin Sketch',18))
    title_label.place(relx=0.5,rely=0.25,anchor='center')

    web_entry1 = tk.Entry(root,font=('Cabin Sketch',15))
    web_entry1.place(relx=0.5,rely=0.5,anchor='center')
    btnRead=tk.Button(root, height=1, width=10,bd=4,bg='white', text="Shorten", command=shorten)
    btnRead.place(relx=0.5,rely=0.7,anchor='center')
    root.mainloop()

def google():
    webbrowser.open('www.google.com')

def bing():
    webbrowser.open('www.bing.com')
    
def yahoo():
    webbrowser.open("www.yahoo.com")
    
def facebook():
    webbrowser.open("www.facebook.com")

def twitter():
    webbrowser.open("www.twitter.com")

def youtube():
    webbrowser.open("www.youtube.com")

def instagram():
    webbrowser.open("www.instagram.com")
    
def nps():
    webbrowser.open("https://npsrnr.com/")

def customopen():
    url = url_entry2.get()
    if url == '':
        showerror('Invalid',' Please Enter A URL')
        web_entry1.delete(0,tk.END)
        return
    try:
        webbrowser.open(url)
    except Exception as e:
        return
    
def custom():
    global url_entry2
    root = tk.Tk()
    root.title('Custom Link')
    root.geometry('400x300')

    title_label = tk.Label(root,text='ENTER LINK BELOW',font=('Cabin Sketch',18))
    title_label.place(relx=0.5,rely=0.25,anchor='center')

    url_entry2 = tk.Entry(root,font=('Cabin Sketch',15))
    url_entry2.place(relx=0.5,rely=0.5,anchor='center')
    btnRead=tk.Button(root, height=1, width=10, bd=4,bg='white',text="Enter", command=customopen)
    btnRead.place(relx=0.5,rely=0.7,anchor='center')
    root.mainloop()


def webbrowsermain():
    global google,bing,yahoo,npsrnr,instagram,twitter,youtube,facebook
    #creating root window
    root = tk.Tk()
    root.title("WebBrowsers")
    root.geometry("330x300")

    tk.Label(root, text="WEBROWSERS",font=('Cabin Sketch',15)).place(relx=0.5,rely=0.07,anchor='center')
    tk.Label(root,text="Select website",font=('Cabin Sketch',15)).place(relx=0.5,rely=0.15,anchor='center')

    #buttons
    google =tk.Button(root,height=1, width=9,text="GOOGLE",command=google,bd=4, font=('Cabin Sketch',15),fg='white',bg='black')
    google.place(relx=0.3,rely=0.31,anchor='center')
    
    custom1 = tk.Button(root,height=1, width=9,text="CUSTOM", command=custom,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    custom1.place(relx=0.7,rely=0.85,anchor='center')
    
    yahoo = tk.Button(root,height=1, width=9,text="YAHOO", command=yahoo,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    yahoo.place(relx=0.3,rely=0.49,anchor='center')
    
    facebook = tk.Button(root,height=1, width=9, text="FACEBOOK", command=facebook,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    facebook.place(relx=0.7,rely=0.49,anchor='center')
    
    twitter = tk.Button(root, height=1, width=9,text="TWITTER", command=twitter,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    twitter.place(relx=0.3,rely=0.67,anchor='center')
    
    youtube = tk.Button(root, height=1, width=9,text="YOUTUBE", command=youtube,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    youtube.place(relx=0.7,rely=0.67,anchor='center')
    
    instagram = tk.Button(root,height=1, width=9, text="INSTAGRAM", command=instagram,bd=4,font=('Cabin Sketch',15),fg='white',bg='black')
    instagram.place(relx=0.3,rely=0.85,anchor='center')
    
    npsrnr=tk.Button(root,height=1, width=9, text="NPS-R", command=nps,font=('Cabin Sketch',15),bd=4,fg='white',bg='black')
    npsrnr.place(relx=0.7,rely=0.31,anchor='center')

    
    #running the mainloop()
    root.mainloop()

    
# main

menu = tk.Tk()
menu.title('Menu')
menu.geometry('400x400')
bg = tk.PhotoImage(file='Background.png')
bg_lab = tk.Label(menu,image=bg)
bg_lab.place(x=-200,y=-200)

Domain_button=tk.Button(menu, height=1, width=20, text="Domain Checker Tool", command=domaincheckmain,bd=8,bg='floral white',fg='black',font=('Cabin Sketch',18))
Domain_button.place(relx=0.5,rely=0.3,anchor='center')

short_button=tk.Button(menu, height=1, width=20, text="Shortener Tool", command=linkshortenermain,bd=8,bg='floral white',fg='black',font=('Cabin Sketch',18))
short_button.place(relx=0.5,rely=0.5,anchor='center')

browser_button=tk.Button(menu, height=1, width=20, text="Web Browser", command=webbrowsermain,bd=8,bg='floral white',fg='black',font=('Cabin Sketch',18))
browser_button.place(relx=0.5,rely=0.7,anchor='center')
menu.mainloop()




    

