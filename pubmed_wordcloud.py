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
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
# from lxml import etree

# setup headless browser
chromedriver = os.getcwd() + '/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chromedriver,options=chrome_options)

# start page for pubmed
keyword = 'Yun-Kai Zhang'
size = 50
url = 'https://pubmed.ncbi.nlm.nih.gov/?term={}&sort=date&size={}'.format(
	keyword,size)
browser.get(url)

text_list = []
all_titles = browser.find_elements_by_xpath(
	'//a[@class="docsum-title"]')
for i in range(0,len(all_titles)):
	all_titles = browser.find_elements_by_xpath(
	'//a[@class="docsum-title"]')
	all_titles[i].click()
	try:
		abstract = browser.find_elements_by_xpath(
			'//div[@class="abstract-content selected"]/p')
		text = ''
		for j in range(0,len(abstract)):
			text = text + abstract[j].text
	except:
		pass
		print(i)
	text_list.append(text)
	browser.back()

# stitch all abstracts together
abstract_text = '\n'.join(text_list)

plt.figure(figsize=(8,5))

# Create word cloud
stopwords = set(STOPWORDS)
# stopwords.update(['osimertinib','treatment','patient',
# 	'survival','NSCLC'])

wordcloud = WordCloud(
	width=800,
	height=500,
	max_font_size=100,
	max_words=150,
	background_color='white',
	collocations=False,
	stopwords=stopwords).generate(abstract_text)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('cloud.png',dpi=300)

