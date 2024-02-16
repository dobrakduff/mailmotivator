import smtplib
import datetime as dt
import random

my_email = "yourmail@gmail.com"
password = "yourpassword"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="yourmail@gmail.com",msg="hello")

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()  # Read all lines from the file into a list
        random_quote = random.choice(quotes)  # Choose a random quote from the list
        print(random_quote)

    connection.sendmail(from_addr=my_email, to_addrs="yourmail@gmail.com", msg=random_quote)


connection.close()