import csv
import os
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing required modules. Install them using:")
    print("pip install beautifulsoup4 requests")
    exit(1)

class CelebrationScraper:
    def __init__(self, url):
        self.url = url

    def welcome_msg(self):
        print("\n=== Celebration Scraper ===\n")
        print("Scraping Greek name day and saving to CSV...\n")

    def validate_url(self):
        try:
            response = requests.head(self.url, allow_redirects=True, timeout=5)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Could not reach the URL: {e}")
            return False

    def start_scraper(self, response):
        try:            
            soup = BeautifulSoup(response.text, 'html.parser')

            table_div = soup.find(id="table2")
            table_rows = table_div.find_all('tr')
            table_row_3rd = table_rows[2]
            div_c_name = table_row_3rd.find_all('div', class_="name") 
            
            celebration_names = []

            for div in div_c_name:
                links = div.find_all('a')
                for link in links:
                    names = link.text.strip()    
                    celebration_names.append(names)  
            celebration_name = ', '.join(celebration_names)
            
            if celebration_name:
                today = datetime.now().strftime("%Y-%m-%d")
                self.save_to_csv(today, celebration_name)
            else:
                print("Could not find the celebration element in the page.")
        except Exception as e:
            print(f"Could not find the celebration text: {e}")

    def save_to_csv(self, date, names):
        file_exists = os.path.exists("celebration-scraper.csv")

        with open("celebration-scraper.csv", "a", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["date", "celebration"])
            writer.writerow([date, names])
            print(f"Saved to CSV: {date} - {names}")

    def run(self):
        self.welcome_msg()
        if self.validate_url():
            response = requests.get(self.url)
            self.start_scraper(response)
        else:
            print("Aborting due to unreachable URL.")

if __name__ == "__main__":
    scraper = CelebrationScraper("https://www.eortologio.net/")
    scraper.run()