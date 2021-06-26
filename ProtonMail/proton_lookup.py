import re
import requests
from datetime import datetime

email_address = input("Enter an email: ")
api = "https://api.protonmail.ch/pks/lookup?op=index&search=" + email_address

try:
    response = requests.get(api).text
    if "info:1:0" not in response:
        timestamp = int(re.search("(?<=:)([0-9]{0,})(?=::)", response).group(0))
        dt_object = datetime.fromtimestamp(timestamp)
        print(f"The creation date of {email_address} is: {dt_object}")
    else:
        print(f"No creation date found for: {email_address}")

except:
    print("An exception occurred because of a connection error or invalid input.")
