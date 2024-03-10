import requests 
from bs4 import BeautifulSoup 
import pdfkit
import sys
import os

initial_url = sys.argv[1]

r = requests.get(initial_url) 

soup = BeautifulSoup(r.content, 'html.parser')   

title = soup.title.string

links = soup.find_all('a', attrs={"class": 'wprm-recipe-print'})

print_link_url = links[0]['href']

print(print_link_url)

r2 = requests.get(print_link_url)

soup2 = BeautifulSoup(r2.content, 'html.parser') 

string = ""

header = soup2.find(id="wprm-print-header-main")

header.decompose()

header_options = soup2.find(id="wprm-print-header-options")

header_options.decompose()

nutrition = soup2.find(class_="wprm-nutrition-label-container")

nutrition.decompose()

nutrition_header = soup2.find(class_="wprm-recipe-nutrition-header")

nutrition_header.decompose()

recipe_meta = soup2.find_all(class_="wprm-recipe-meta-container")

for x in recipe_meta: 
    x.decompose()

recipe_images = soup2.find_all("img")

for x in recipe_images: 
    x.decompose()


print(soup2)

temp_html_file = f"./output_folder/{title}.html"

with open(temp_html_file, "w") as file:
    file.write(str(soup2))

pdfkit.from_file(temp_html_file, f"./output_folder/{title}.pdf")

os.remove(temp_html_file)