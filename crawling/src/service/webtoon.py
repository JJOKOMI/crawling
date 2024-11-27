from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://comic.naver.com/webtoon")
    sleep(1)

    days=driver.find_elements(by=By.CSS_SELECTOR,
                         value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a')
    for day in days[1:8]:
        driver.execute_script("arguments[0].scrollIntoView(true);", day)
        day.click()

        print(day.text)

        webtoonTitles = driver.find_elements(by=By.CSS_SELECTOR,
                                             value='#content > div:nth-child(1) > ul > li > div > a > span')

        for webtoonTitle in webtoonTitles:
            print(webtoonTitle.text)

def run2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://comic.naver.com/webtoon")
    sleep(1)

    days = driver.find_elements(by=By.CSS_SELECTOR,
                                value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a')
    for day in days[1:8]:
        driver.execute_script("arguments[0].scrollIntoView(true);", day)
        day.click()

        print(day.text)

        webtoonTitles = driver.find_elements(by=By.CSS_SELECTOR,
                                             value='#container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul > li > div > a > span > span')

        for webtoonTitle in webtoonTitles:
            print(webtoonTitle.text)