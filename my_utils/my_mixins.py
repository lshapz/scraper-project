# from bs4 import BeautifulSoup 

def image_remover(the_soup):
    recipe_images = the_soup.find_all("img")

    for x in recipe_images: 
        x.decompose()

def remove_by_id(the_soup, id_name):
    thing = the_soup.find(id=f"{id_name}")

    if thing:
        thing.decompose()


def remove_by_class(the_soup, class_name):
    thing = the_soup.find_all(class_=f"{class_name}")
    
    if thing:
        for x in thing: 
            x.decompose()
