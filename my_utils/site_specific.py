import requests 
import selenium
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
from my_utils.pdf_maker import pdf_maker
from my_utils.my_mixins import image_remover, remove_by_class, remove_by_id

# def print_simply(url):
    
    # r = requests.get(f"{url}/?print")
    
    # soup = BeautifulSoup(r.content, 'html.parser')   

    # title = soup.title.string
    
    # # print(soup)

    # pdf_maker(title, soup)

    # driver = selenium.webdriver.Firefox()

    # driver.get(url)

    # title_elem = driver.find_element(By.TAG_NAME, "title")

    # title = title_elem.get_attribute('innerHTML')

    # button_container = driver.find_element(By.CLASS_NAME, 'print-button')

    # button = button_container.find_element(By.TAG_NAME, "button")

    # button.click()

# this is going to need more work because the button click prompts the system print dialog

    # driver.quit()


    # print-button
    # return ""

def print_ersp(url):
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')   
    
    title = soup.title.string

    links = soup.find_all(attrs={"class", "ERSPrintBtn"})
    
    new_url = links[0]["href"]

    r2 = requests.get(new_url)

    soup2 = BeautifulSoup(r2.content, 'html.parser') 

    print(soup2)

    image_remover(soup2)

    remove_by_class(soup2, "ERSTimes")

    pdf_maker(title, soup2)


def print_itr(url):

    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')   
    
    title = soup.title.string

    for link in soup.find_all(attrs={"class":  'print-itr'}):
        new_url = link.find('a')['href']

    r2 = requests.get(new_url)

    soup2 = BeautifulSoup(r2.content, 'html.parser') 

    remove_by_class(soup2, 'itr-print-button')

    remove_by_class(soup2, "itr-nutrition")

    image_remover(soup2)

    pdf_maker(title, soup2)


def print_wprm(url): 

    r = requests.get(url) 

    soup = BeautifulSoup(r.content, 'html.parser')   

    title = soup.title.string

    links = soup.find_all('a', attrs={"class": 'wprm-recipe-print'})

    print_link_url = links[0]['href']

    r2 = requests.get(print_link_url)

    soup2 = BeautifulSoup(r2.content, 'html.parser') 

    remove_by_id(soup2, "wprm-print-header-options")

    remove_by_class(soup2, "wprm-nutrition-label-container")

    remove_by_class(soup2, "wprm-recipe-nutrition-header")

    remove_by_class(soup2, "wprm-recipe-meta-container")

    image_remover(soup2)

    pdf_maker(title, soup2)


def print_all(url):
    # you cannot navigate to the print-friendly allrecipes page directly through "requests" so we're using Selenium 

    driver = selenium.webdriver.Firefox()

    driver.get(url)

    title_elem = driver.find_element(By.TAG_NAME, "title")

    title = title_elem.get_attribute('innerHTML')

    print_button = driver.find_elements(By.CLASS_NAME, 'mntl-print-button__btn')
    print(print_button)
    if (print_button != []): 
        driver.find_element(By.CLASS_NAME, 'mntl-print-button__btn').click()
    else:
        print("this is a list not a recipe!")
        return ""

    ingredients = driver.find_element(By.ID, 'mntl-lrs-ingredients_1-0').get_attribute("outerHTML")

    directions = driver.find_element(By.ID, "recipe__steps_1-0").get_attribute("outerHTML")

    print(directions)

    save = ingredients + directions

    driver.quit()

    soup = BeautifulSoup(save, 'html.parser')  
    
    image_remover(soup)

    pdf_maker(title, soup)

    

