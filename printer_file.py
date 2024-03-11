import requests 
import selenium
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
from my_utils.site_specific import print_all, print_wprm, print_itr, print_ersp


def use_url(url): 
    r = requests.get(url) 
    print(url)
    soup = BeautifulSoup(r.content, 'html.parser')   

    wprm_print_links = soup.find_all("a", attrs={"class": "wprm-recipe-print"})
    itr_print_links = soup.find_all(attrs={"class": "print-itr"})
    ersp_print_links = soup.find_all(attrs={"class", "ERSPrintBtn"})
    error_divs_cloudflare = soup.find_all(attrs={"class": "cf-error-details"})
    error_message_scoots = "blocked" in soup.find_all("h1")[0].contents[0]

    if "allrecipes" in url: 
        print(url)
        print_all(url)
    elif wprm_print_links:
        print("WPRM")
        print_wprm(url)
    elif itr_print_links: 
        print("ITR")
        print_itr(url)
    elif ersp_print_links: 
        print("ERSP")
        print_ersp(url)
    elif len(error_divs_cloudflare) > 0 or error_message_scoots:
        print("I don't think we can scrape this one, bud") 
        print(url)
    else:    
        print("not the right format! we'll get there though")
        print(url)
        stripped_url = " ".join(url.split("/"))
        with open(f"./{stripped_url}.html", "w") as file:
            file.write(str(soup))
