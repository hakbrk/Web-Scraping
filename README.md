# Web-Scraping
Mission to Mars web scraping and database project

# Quick Start

1) Open the file app.py ins VS a code and run this code.
2) Open the local host browser that was initiated by Flask.
3) Click on the "Get Data! button which will update the page with current photos and data.

# Files included in repository
* mission_to_mars.ipynb - File contains scrapping code in Jupyter Notebook form.  This code was used to develop and test the Python Code located in scrape_mars.
* app.py - File contains Python code which initiates Flask apps and functions to initiate the scrape_mars function.
* scrape_mars.py - File contains Pythin code used to initiate Chromedriver sessions and scrape requested data.
* mars_weather_scrape.ipynb - This was a departure from the assignment and a bit of fun to see if I could scrape the historical weather data from the mars rover twitter page.  This code scrapped 600 twitter posts, discards any that do not contain weather data.  It then parses the results for specific weather data.  The long term plan was to include this as a graph on the Mission to Mars data page but time got the best of me, maybe something I will add later.  I would not recommend running the code as it can take some time to scrape the data.  The results of the code can be found in the csv file mars_weather.
* mars_weather.csv - Data parsed from mars_weatehr_scrape.ipynb
