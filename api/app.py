import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    # Hacker News headlines and links
    hn_headlines, hn_links = scrape_hacker_news_today()
    hn_headlines_links = list(zip(hn_headlines, hn_links))

    # TechCrunch headlines and links
    tc_headlines, tc_links = scrape_techcrunch()
    tc_headlines_links = list(zip(tc_headlines, tc_links))

    # Slashdot headlines and links
    sd_headlines, sd_links = scrape_slashdot()
    sd_headlines_links = list(zip(sd_headlines, sd_links))

    # Print debugging
    for headline, link in hn_headlines_links:
        print(headline, link)

    for headline, link in tc_headlines_links:
        print(headline, link)

    for headline, link in sd_headlines_links:
        print(headline, link)

    return render_template("index.html", hn_headlines_links=hn_headlines_links, tc_headlines_links=tc_headlines_links, sd_headlines_links=sd_headlines_links)


# Scrape Hacker News
def scrape_hacker_news_today():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    hn_headlines = []
    hn_links = []

    # Get headlines
    for i, headline in enumerate(soup.find_all("span", class_="titleline")):
        if i >= 10:  # Stop after scraping 10 headlines
            break
        hn_headlines.append(headline.text)

        # Get headline links
        a = headline.find("a")
        if a is not None:
            hn_links.append(a.get("href"))

    return hn_headlines, hn_links


# Scrape Tech Crunch
def scrape_techcrunch():
    url = "https://techcrunch.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tc_headlines = []
    tc_links = []

    # Get headlines
    for i, headline in enumerate(soup.find_all("h2")):
        if i >= 10:  # Stop after scraping 10 headlines
            break
        tc_headlines.append(headline.text)

        # Get headline links
        a = headline.find("a")
        if a is not None:
            tc_links.append(a.get("href"))

    return tc_headlines, tc_links


# Scrape Slashdot
def scrape_slashdot():
    url = "https://slashdot.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    sd_headlines = []
    sd_links = []

    # Get headlines
    for i, headline in enumerate(soup.find_all("span", class_="story-title")):
        if i >= 10:  # Stop after scraping 10 headlines
            break
        sd_headlines.append(headline.text)

        # Get headline links
        a = headline.find("a")
        if a is not None:
            sd_links.append(a.get("href"))

    return sd_headlines, sd_links


if __name__ == "__main__":
    # Automatically reloads dev server when Python file changes
    app.run(debug=True)
