import datetime
import os
import random
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv, dotenv_values
import pandas as pd

load_dotenv()

smtp_host = os.getenv("SMTP_HOST")
smtp_port = int(os.getenv("SMTP_PORT"))
smtp_pass = os.getenv("SMTP_PASSWORD")
smtp_email = os.getenv("SMTP_EMAIL")

dir_path = os.path.dirname(os.path.realpath(__file__)) # Get the directory of the current script
birthdays_filepath = dir_path + "/data/birthdays.csv" # Get the filepath of the birthdays csv file
today = datetime.date.today() # Get today's date

def read_csv_file(file_path):
    """
    Read a csv file and return a pandas dataframe
    :param file_path: filepath to the csv file
    :return: dataframe of the csv file
    """
    try:
        df = pd.read_csv(file_path) # Read the csv file
        return df # Return the dataframe
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
def check_today_birthday(df):
    """
    check if today is a birthday. if true, so return a list of the birthdays
    :param df: dataframe of birthdays
    :return: list of birthdays
    """
    list_birthday = []
    month_today = today.month # Get the month of today
    day_today = today.day # Get the day of today

    for index, row in df.iterrows(): # Iterate through the dataframe
        month_birthday = row["month"] # Get the month of the birthday
        day_birthday = row["day"] # Get the day of the birthday

        if month_today == month_birthday and day_today == day_birthday: # Check if today is a birthday
            list_birthday.append([row["name"], row["email"], row["year"]]) # Create a list of the birthday's name, email, and year

    return list_birthday # Return the list of birthdays
def get_random_letter():
    """
    get a random letter from the templates
    :return: letter
    """
    files = [f for f in os.listdir(dir_path + "/data/letter_templates") if os.path.isfile(os.path.join(dir_path + "/data/letter_templates", f))] # Get a list of all the files in the templates directory
    file_path = os.path.join(dir_path + "/data/letter_templates", random.choice(files)) # Return a random file from the list
    path = Path(file_path) # Convert the file path to a Path object

    return path.read_text() # Return the contents of the file
def replace_letter_placeholders(template, birthday):
    """
    Replace the placeholders in the email template with the birthday's name and year
    :param template: letter template
    :param birthday: personal information of the birthday
    :return: letter
    """
    return template.replace("[NAME]", birthday[0]).replace("[AGE]", str(today.year - int(birthday[2]))) # Replace the placeholders in the email template with the birthday's name and year
def send_email(letter, birthday):
    """
    send the email
    :param letter: letter
    :param birthday: personal information of the birthday
    """
    msg = EmailMessage()
    msg["Subject"] = "Uma mensagem muito especial!"
    msg["From"] = smtp_email
    msg["To"] = birthday[1]
    msg.set_content(letter, charset="utf-8")

    with smtplib.SMTP(smtp_host, smtp_port) as conn:  # Create an SMTP connection
        conn.starttls()  # Enable TLS encryption
        conn.login(user=smtp_email, password=smtp_pass)  # Log in to the SMTP server
        conn.send_message(msg) # Send the email

birthdays = read_csv_file(birthdays_filepath) # Read the birthdays csv file
birthdays_today = check_today_birthday(birthdays) # Check if today is a birthday

if not len(birthdays_today) == 0: # if today is a birthday
    for birthday in birthdays_today: # for each birthday
        template = get_random_letter() # pick a random letter from templates
        letter = replace_letter_placeholders(template, birthday) # replace the placeholders in the email template with the birthday's name and year
        send_email(letter, birthday) # send the email
        print(f"Send email to {birthday[1]}")
else:
    print("No birthdays today")