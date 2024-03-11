import requests 
from bs4 import BeautifulSoup 
from printer_file import use_url

# blocked_urls = ["ambitiouskitchen", "tastesbetterfromscratch"]

search_term = input("what recipe ar eyou searching for? \n")

search_list = search_term.split(" ")
search_string = "+".join(search_list) + "+recipe"

r = requests.get(f"https://google.com/search?q={search_string}") 

soup = BeautifulSoup(r.content, 'html.parser')   

links = soup.find_all("a")

def various_filters(link): 
    the_href = link["href"] 
    if link.parent.name == "span":
        if "https" in the_href and "google" not in the_href:
            return True

filtered_links = filter(various_filters, links)

def map_func(input_var): 
    split_list = input_var["href"].split("/url?q=")
    if len(split_list) > 0:
        # print(split_list)
        return split_list[1].split("&sa")[0]
    else:
        return ""

mapped_links = map(map_func, list(filtered_links))
for x in mapped_links:
     print(x)
     use_url(x)


