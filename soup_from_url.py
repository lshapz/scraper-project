import requests 
from bs4 import BeautifulSoup 
import pdfkit
import sys
import os
from printer_file import use_url


initial_url = sys.argv[1]

use_url(initial_url)