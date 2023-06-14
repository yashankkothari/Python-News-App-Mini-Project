import requests
import smtplib
import json
from tkinter import *
from tkinter import messagebox, simpledialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "1cf868802b6545909bd990752e217368"

my_email = "news.python.project@gmail.com"
password = "kyexhlliyfyttnxi"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

root = Tk()
root.title("News App")

def onClick():
    query = news_input.get()
    if not query:
        messagebox.showinfo("Warning", message="Please type something first.")
        return

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    if not articles:
        messagebox.showinfo("No Results", message="No news articles found.")
        return

    message = ""
    for article in articles[:3]:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")
        if title and description and url:
            message += f"{title}\n{description}\n{url}\n\n"

    output.configure(state='normal')
    output.delete(1.0, END)
    output.insert(END, message)
    output.configure(state='disable')

    news_box = messagebox.askyesno(title="NEWS", message=f"{message}\n\nDo you want it via email?")
    if news_box:
        email_input = simpledialog.askstring("Email Input", "Please enter your email address")
        if email_input:
            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = email_input
            msg["Subject"] = query

            body = MIMEText(message.encode("utf-8"), "plain", "utf-8")
            msg.attach(body)

            connection.sendmail(from_addr=my_email, to_addrs=email_input, msg=msg.as_string())
            messagebox.showinfo("Success", message="Mail Sent")
        else:
            messagebox.showinfo("No Email Address", message="No email address provided.")

news_input = Entry(width=50)
news_input.grid(column=1, row=2)
news_input.focus()

button = Button(root, text="SEARCH", command=onClick, height=2, width=10, bg="coral1", font="bold")
button.grid(column=1, row=3)

title = Label(root, text="Type to get News", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=GROOVE, bg="coral", fg="black")
title.grid(column=1, row=0)

news_title = Label(root, text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=GROOVE, width=40)
news_title.grid(column=1, row=4, columnspan=3)
output = Text(root, height=20, width=80, bg="pink", padx=15, state='disable', wrap='word')
output.grid(column=1, row=5)

name_label = Label(root, text="Made By Yashank Kothari - 16010122089", font=("times new roman", 16), pady=10)
name_label.grid(column=1, row=7)

root.config(bg='misty rose')
root.mainloop()import requests
import smtplib
import json
from tkinter import *
from tkinter import messagebox, simpledialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "1cf868802b6545909bd990752e217368"

my_email = "news.python.project@gmail.com"
password = "kyexhlliyfyttnxi"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

root = Tk()
root.title("News App")

def onClick():
    query = news_input.get()
    if not query:
        messagebox.showinfo("Warning", message="Please type something first.")
        return

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    if not articles:
        messagebox.showinfo("No Results", message="No news articles found.")
        return

    message = ""
    for article in articles[:3]:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")
        if title and description and url:
            message += f"{title}\n{description}\n{url}\n\n"

    output.configure(state='normal')
    output.delete(1.0, END)
    output.insert(END, message)
    output.configure(state='disable')

    news_box = messagebox.askyesno(title="NEWS", message=f"{message}\n\nDo you want it via email?")
    if news_box:
        email_input = simpledialog.askstring("Email Input", "Please enter your email address")
        if email_input:
            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = email_input
            msg["Subject"] = query

            body = MIMEText(message.encode("utf-8"), "plain", "utf-8")
            msg.attach(body)

            connection.sendmail(from_addr=my_email, to_addrs=email_input, msg=msg.as_string())
            messagebox.showinfo("Success", message="Mail Sent")
        else:
            messagebox.showinfo("No Email Address", message="No email address provided.")

news_input = Entry(width=50)
news_input.grid(column=1, row=2)
news_input.focus()

button = Button(root, text="SEARCH", command=onClick, height=2, width=10, bg="coral1", font="bold")
button.grid(column=1, row=3)

title = Label(root, text="Type to get News", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=GROOVE, bg="coral", fg="black")
title.grid(column=1, row=0)

news_title = Label(root, text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=GROOVE, width=40)
news_title.grid(column=1, row=4, columnspan=3)
output = Text(root, height=20, width=80, bg="pink", padx=15, state='disable', wrap='word')
output.grid(column=1, row=5)

name_label = Label(root, text="Made By Yashank Kothari - 16010122089", font=("times new roman", 16), pady=10)
name_label.grid(column=1, row=7)

root.config(bg='misty rose')
root.mainloop()import requests
import smtplib
import json
from tkinter import *
from tkinter import messagebox, simpledialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "1cf868802b6545909bd990752e217368"

my_email = "news.python.project@gmail.com"
password = "kyexhlliyfyttnxi"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

root = Tk()
root.title("News App")

def onClick():
    query = news_input.get()
    if not query:
        messagebox.showinfo("Warning", message="Please type something first.")
        return

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    if not articles:
        messagebox.showinfo("No Results", message="No news articles found.")
        return

    message = ""
    for article in articles[:3]:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")
        if title and description and url:
            message += f"{title}\n{description}\n{url}\n\n"

    output.configure(state='normal')
    output.delete(1.0, END)
    output.insert(END, message)
    output.configure(state='disable')

    news_box = messagebox.askyesno(title="NEWS", message=f"{message}\n\nDo you want it via email?")
    if news_box:
        email_input = simpledialog.askstring("Email Input", "Please enter your email address")
        if email_input:
            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = email_input
            msg["Subject"] = query

            body = MIMEText(message.encode("utf-8"), "plain", "utf-8")
            msg.attach(body)

            connection.sendmail(from_addr=my_email, to_addrs=email_input, msg=msg.as_string())
            messagebox.showinfo("Success", message="Mail Sent")
        else:
            messagebox.showinfo("No Email Address", message="No email address provided.")

news_input = Entry(width=50)
news_input.grid(column=1, row=2)
news_input.focus()

button = Button(root, text="SEARCH", command=onClick, height=2, width=10, bg="coral1", font="bold")
button.grid(column=1, row=3)

title = Label(root, text="Type to get News", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=GROOVE, bg="coral", fg="black")
title.grid(column=1, row=0)

news_title = Label(root, text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=GROOVE, width=40)
news_title.grid(column=1, row=4, columnspan=3)
output = Text(root, height=20, width=80, bg="pink", padx=15, state='disable', wrap='word')
output.grid(column=1, row=5)

name_label = Label(root, text="Made By Yashank Kothari - 16010122089", font=("times new roman", 16), pady=10)
name_label.grid(column=1, row=7)

root.config(bg='misty rose')
root.mainloop()import requests
import smtplib
import json
from tkinter import *
from tkinter import messagebox, simpledialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "1cf868802b6545909bd990752e217368"

my_email = "news.python.project@gmail.com"
password = "kyexhlliyfyttnxi"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

root = Tk()
root.title("News App")

def onClick():
    query = news_input.get()
    if not query:
        messagebox.showinfo("Warning", message="Please type something first.")
        return

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    if not articles:
        messagebox.showinfo("No Results", message="No news articles found.")
        return

    message = ""
    for article in articles[:3]:
        title = article.get("title", "")
        description = article.get("description", "")
        url = article.get("url", "")
        if title and description and url:
            message += f"{title}\n{description}\n{url}\n\n"

    output.configure(state='normal')
    output.delete(1.0, END)
    output.insert(END, message)
    output.configure(state='disable')

    news_box = messagebox.askyesno(title="NEWS", message=f"{message}\n\nDo you want it via email?")
    if news_box:
        email_input = simpledialog.askstring("Email Input", "Please enter your email address")
        if email_input:
            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = email_input
            msg["Subject"] = query

            body = MIMEText(message.encode("utf-8"), "plain", "utf-8")
            msg.attach(body)

            connection.sendmail(from_addr=my_email, to_addrs=email_input, msg=msg.as_string())
            messagebox.showinfo("Success", message="Mail Sent")
        else:
            messagebox.showinfo("No Email Address", message="No email address provided.")

news_input = Entry(width=50)
news_input.grid(column=1, row=2)
news_input.focus()

button = Button(root, text="SEARCH", command=onClick, height=2, width=10, bg="coral1", font="bold")
button.grid(column=1, row=3)

title = Label(root, text="Type to get News", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=GROOVE, bg="coral", fg="black")
title.grid(column=1, row=0)

news_title = Label(root, text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=GROOVE, width=40)
news_title.grid(column=1, row=4, columnspan=3)
output = Text(root, height=20, width=80, bg="pink", padx=15, state='disable', wrap='word')
output.grid(column=1, row=5)

name_label = Label(root, text="Made By Yashank Kothari - 16010122089", font=("times new roman", 16), pady=10)
name_label.grid(column=1, row=7)

root.config(bg='misty rose')
root.mainloop()
