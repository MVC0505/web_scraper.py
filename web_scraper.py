import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"   

def scrape_headlines():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except Exception as e:
        print("Error fetching the website:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

    if not headlines:
        print("No headlines found. Try changing the tag or website.")
        return

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            file.write(h + "\n")

    print("Scraping complete. Headlines saved in headlines.txt")

if __name__ == "__main__":
    scrape_headlines()
