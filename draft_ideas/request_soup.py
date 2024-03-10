import requests 
from bs4 import BeautifulSoup 
import pdfkit

# Making a GET request 
r = requests.get('https://downshiftology.com/recipes/chicken-soup/') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
  
# # Getting the title tag 
# print(soup.title) 
  
# # Getting the name of the tag 
# print(soup.title.name) 
  
# # Getting the name of parent tag 
# print(soup.title.parent.name) 

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

# print(soup2)

# # button = soup2.find_all(id="wprm-print-button-print")

# # print(id)
# # print(button)
# # pdfkit.from_url(print_link_url, "soup_recipe.pdf") // this prints the whole "print" page including options for size and nutrition facts and stuff


with open("output1.html", "w") as file:
    file.write(str(soup2))


pdfkit.from_file("output1.html", "soup_recipe.pdf")
