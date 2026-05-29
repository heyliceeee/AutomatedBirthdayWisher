import datetime
import os
import smtplib
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

print(read_csv_file(birthdays_filepath))