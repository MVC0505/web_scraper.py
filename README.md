This project is a simple Python script that scrapes top news headlines from a target news website. The script uses the requests library to fetch HTML content and BeautifulSoup to parse and extract headline tags. All collected headlines are saved in a text file for further use.

Features

- Fetches HTML content from a news website

- Extracts headlines from &lt;h2&gt; tags (customizable)

- Saves all headlines into headlines.txt

- Easy to modify for different websites or tags

Requirements

- Python 3.x

- requests library

- beautifulsoup4 library

Install dependencies:

    pip install requests beautifulsoup4

How It Works

- The script sends a GET request to the target news website

- BeautifulSoup parses the HTML

- All &lt;h2&gt; tag text content is extracted as headlines

- Headlines are written line-by-line into headlines.txt

How to Run

- Save the script as scraper.py

- Make sure dependencies are installed

Run the script:

    python scraper.py


After running, check the generated headlines.txt file

File Structure

    news_scraper/
      scraper.py
      headlines.txt
      README.md

Customization

Change the URL variable in the script to scrape a different site

Modify the tag selector in:

    soup.find_all("h2")
