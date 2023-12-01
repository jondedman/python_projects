# https://www.andertons.co.uk/line-6-helix-hx-stomp-xl-silver-edition-8-switch-effects-processor
from bs4 import BeautifulSoup
import requests
import smtplib
import os
import dotenv

dotenv.load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

# NB if scraping amazon, you need to set the headers to a browser user agent. forexample:
# headers = {
#     "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
#     "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
# }

url = "https://www.andertons.co.uk/line-6-helix-hx-stomp-xl-silver-edition-8-switch-effects-processor"

response = requests.get(url)
# if amazon then you will need to pass in the headers=headers parameter
# and instead of the html.parser, you will need to use lxml
# for example: soup = BeautifulSoup(response.text, "lxml")
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="o-price").getText()
price_without_currency = price.split("£")[1]

if float(price_without_currency) < 700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        msg=f"Subject:Line 6 HX Stomp XL Price Alert!\n\nThe Line 6 HX Stomp XL is now £{price_without_currency}\n{url}"
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=msg.encode("utf-8"),
        )
    print("Email sent")

    # Note: this program could be expanded to check the results of the item on various websites and then send an email. It can also be scheduled to run at a certain time by using launchd on mac or task scheduler on windows.
