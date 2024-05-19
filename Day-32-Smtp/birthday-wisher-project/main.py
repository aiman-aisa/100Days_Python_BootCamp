##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd

birthday_df = pd.read_csv(r"Day-32-Smtp\birthday-wisher-project\birthdays.csv")

def send_letter(name):
    letter_no = random.choice(range(1,4))
    letter_file_path = f"Day-32-Smtp\\birthday-wisher-project\\letter_templates\\letter_{letter_no}.txt"
    with open(letter_file_path) as letter_file:
        letter = letter_file.read()
    invite_letter = letter.replace("[NAME]", name)
    
    my_email = "aiman.ab.ghapar@gmail.com"
    password = ""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="raigaex95@gmail.com", 
            msg=f"Subject:Happy Birthday {name}\n\n{invite_letter}"
            )
        
today = dt.datetime.now()
month_now = today.month
day_now = today.day

for index, row in birthday_df.iterrows():
    if int(row['month']) == month_now and int(row['day']) == day_now:
        send_letter(row['name'])




