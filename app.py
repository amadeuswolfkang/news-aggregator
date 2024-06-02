import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    headlines, links = scrape_hacker_news_today()
    headlines_links = list(zip(headlines, links))

    # Print debugging
    for headline, link in headlines_links:
        print(headline, link)

    return render_template("index.html", headlines_links=headlines_links)


# Scrape Hacker News
def scrape_hacker_news_today():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []
    links = []

    # Get headlines
    for i, headline in enumerate(soup.find_all("span", class_="titleline")):
        if i >= 10:  # Stop after scraping 5 headlines
            break
        headlines.append(headline.text)

        # Get headline links
        a = headline.find("a")
        if a is not None:
            links.append(a.get("href"))

    return headlines, links


if __name__ == "__main__":
    # Automatically reloads dev server when Python file changes
    app.run(debug=True)
