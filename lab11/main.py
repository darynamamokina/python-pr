from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://www.pravda.com.ua/archives/')

format_link = lambda day, month, year: f"https://www.pravda.com.ua/archives/date_{day}{month}{year}/"

a = pd.DataFrame(columns=['Date', 'Text'])

def update_a(text, date):
    global a
    a = pd.concat([a, pd.DataFrame({'Date': date, 'Text': [text]})], ignore_index=True)
    a.to_csv('pravda_data.csv', index=False)  

def process_page_news(link, date):
        article = []
        driver.get(link)

        articles = driver.find_elements(By.CSS_SELECTOR, 'div.article.article_list a[href]')

        for article in articles:
            try:
                article_link = article.get_attribute('href')
                if 'epravda.com.ua' in article_link or 'eurointegration.com.ua' in article_link or 'pravda.com.ua' in article_link:
                    driver.get(article_link)
                    main_div = driver.find_elements(By.CSS_SELECTOR, 'div.post__text p')
                    text = [p.text for p in main_div]
                    update_a(text, date)
                elif 'life.pravda.com.ua' in article_link:
                    driver.get(article_link)
                    main_div = driver.find_elements(By.CSS_SELECTOR, 'article.article p')
                    text = [p.text for p in main_div]
                    update_a(text, date)
                else:
                    pass
                driver.back()
            except StaleElementReferenceException:
                pass
    
for year in [2023]:
    for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]:
        process_page_news(format_link("10", month, year), f'10-{month}-{year}')


driver.close()
