
#Import required libraries and modules
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import pymongo

#Create browser path for chromedriver
#executable_path = {'executable_path': 'chromedriver.exe'}


def init_browser():
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    # Scrape headline and paragraph from https://mars.nasa.gov
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    browser.is_element_present_by_css('content_title', wait_time=1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    browser.is_element_present_by_css('article_teaser_body', wait_time=1)
    news_p = soup.find('div', class_='article_teaser_body').text

    # Scape featured image url from https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL')
    browser.is_element_present_by_css('buttons', wait_time=1)
    browser.find_link_by_partial_text('more info').first.click()
    browser.is_element_present_by_css('main_image', wait_time=1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_title = soup.find('h1', class_='article_title').text
    browser.click_link_by_partial_href('/spaceimages/images/largesize/')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img').get('src')

        # Scrape current mars weather from https://twitter.com/MarsWxReport?lang=en
    url = 'https://twitter.com/MarsWxReport?lang=en'
    browser.visit(url)
    browser.is_text_present('MarsWxReport', wait_time=1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    a=0
    while a<10:
        mars_weather = soup.find_all('p', class_='TweetTextSize')[a].text
        if "low" in mars_weather:
            break
        else:
            a+=1

    # Scrape mars facts table from https://space-facts.com/mars/
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    table_facts = tables[1]
    table_facts.columns = ['', '']
    table_facts
    facts_html = table_facts.to_html(index=False)

    # Scrape hemisphere images urls's from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemispheres = ['Valles', 'Cerberus', 'Schiaparelli', 'Syrtis']
    hemisphere_img_urls = []
    for hemisphere in hemispheres:
        browser.visit(url)
        browser.is_text_present(hemisphere, wait_time=1)
        browser.click_link_by_partial_text(hemisphere)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_='title').text
        img_url = soup.find('a', target='_blank').get('href')
        hemisphere_img_urls.append({'title': title,
                                    'img_url' : img_url})

        # Append data to mars_data dictionary
        mars_data = {
        'news_title' : news_title,
        'news_p' : news_p,
        'featured_image_url' : featured_image_url,
        'mars_weather' : mars_weather,
        'facts_html' : facts_html,
        'hemisphere_img_urls' : hemisphere_img_urls,
        'featured_title' : featured_title
        }

    browser.quit()

    return mars_data




