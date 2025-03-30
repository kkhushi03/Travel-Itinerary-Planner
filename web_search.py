import requests
from bs4 import BeautifulSoup

def fetch_top_attractions(destination):
    """Fetches top attractions for a given destination using web scraping."""
    search_url = f"https://www.google.com/search?q=top+attractions+in+{destination.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    attractions = [a.text for a in soup.find_all("h3")]
    return attractions[:5] if attractions else ["No attractions found."]
