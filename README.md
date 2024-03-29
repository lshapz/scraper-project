# (Beautiful) Soup PDF Scraper for Python

### PDF from URL:

`python3 soup_from.url.py [url]`

i.e. 

`python3 soup_from_url.py https://downshiftology.com/recipes/chicken-soup/`

this will create a cleaned up PDF, with a filename based on the `<title>` of the original recipe, and put it in the `./output folder`. unless the website blocks scrapers. 

### search term 

`python3 searcher.py`

then, when prompted, type the name of the recipe. note that right now, for debugging reasons, any recipe that cannot be converted to pdf will be saved as HTML for the developer to reference later. 

### Todo list for lshapz's reference 

* what if the recipe website is not using the wprm recipe printable software? 
    * figure out parsing steps for other common recipe webiste utilities (continue)
    * make a starter file that determines what software the website is using and conditionally uses the relevant function / module / file  
* what if the recipe website blocks requests/beautiful soup? 
    * exit with an error message?
    * is this where Selenium comes in 
* what if you want a different output folder, say, `~/Documents/recipes`? 
    * make that an optional argument
* relatedly, what if you want to name the file yourself? 
    * make _that_ an optional argument 
* what if you want to do multiple in a row? 
    * if argument is one url, then just do one url
    * if argument is a .txt file with a list of urls, iterate through that file
    * if no argumemnt, input prompt for a url? or just exit with an error? 
* keeps repeating recipes on search because recipe#title_heading comes up
    * make a list of urls already processed and skip if its just a variant? 

## Requirements 

Must have [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) installed locally! 

For Mac, that's as simple as:

`brew install Caskroom/cask/wkhtmltopdf`

#### Initial Installation 
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `pip3 install -r requirements.txt`