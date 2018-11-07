import requests
from bs4 import BeautifulSoup

body = requests.get("https://tesonet.com/career/")

soup = BeautifulSoup(body.text, "html.parser")

tech_id = soup.find(id="tech")
print(f"{tech_id.text}:")
tech_div = tech_id.next_sibling

longest_title = 0
positions = []

for pos in tech_div:
    href = pos.find("a")['href']
    position_title = pos.find("span", {"class": "position-title"}).text
    positions.append((position_title, href))
    if len(position_title) > longest_title:
        longest_title = len(position_title)

for p in positions:
    spaces = longest_title - len(p[0])
    print(f" - {p[0]}" + " " * spaces + f" : {p[1]}")
