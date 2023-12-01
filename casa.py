import csv
from bs4 import BeautifulSoup
import requests

web_url = 'https://www.utep.edu/extendeduniversity/cid/people/'

page_to_scrape = requests.get(web_url)
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

emails = soup.findAll('span', attrs={'class': 'email'})
phones = soup.findAll('span', attrs={'class': 'phone'})


with open('contact_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
   
    csv_writer = csv.writer(csvfile)

    
    csv_writer.writerow(['Email', 'Phone'])

    # Iterate over emails and phones simultaneously
    for email, phone in zip(emails, phones):
        email_text = email.text.strip()
        phone_text = phone.text.strip()

    
        csv_writer.writerow([email_text, phone_text])
        print(f"Email: {email_text}, Phone: {phone_text}")

print("CSV file created successfully.")

