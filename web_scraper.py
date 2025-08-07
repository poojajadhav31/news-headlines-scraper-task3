# web_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f" Failed to fetch page. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all <h2> tags which commonly contain headlines
        headlines = [h2.get_text().strip() for h2 in soup.find_all("h2") if h2.get_text().strip()]
        return headlines

    except Exception as e:
        print(" Error occurred:", e)
        return []

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, headline in enumerate(headlines, start=1):
            file.write(f"{idx}. {headline}\n")
    print(f" Headlines saved to {filename}")

if __name__ == "__main__":
    # Example: scraping from BBC News
    url = "https://www.bbc.com/news"
    print(f" Fetching headlines from {url}...\n")

    headlines = fetch_headlines(url)

    if headlines:
        for h in headlines[:10]:  # show top 10 headlines in terminal
            print(" ", h)
        save_to_file(headlines)
    else:
        print(" No headlines found.")
