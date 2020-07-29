'''
Acquire the most recent 50 abstracts from pubmed of certain 
keywords, make a word cloud for presentation.
Write an output to html.

ver. 0.1
Author: Dr. Yunkai Zhang
Vanderbilt University Medical Center
'''

# import modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
# from lxml import etree

# setup headless browser
chromedriver = os.getcwd() + '/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chromedriver,options=chrome_options)

# start page for pubmed
keyword = 'EGFR+osimertinib'
size = 50
url = 'https://pubmed.ncbi.nlm.nih.gov/?term={}&sort=date&size={}'.format(
	keyword,size)
browser.get(url)

# get all titles from the start page
all_titles = browser.find_elements_by_xpath(
	'//a[@class="docsum-title"]')

for i in range(0,50):
	all_titles[i].click()
	abstract = browser.find_elements_by_xpath(
		'//div[@class="abstract-content selected"]/p')[0]
	print(abstract.text)
	exit()

