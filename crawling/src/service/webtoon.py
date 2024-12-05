import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.repository.webtoon_repository import saveWebtoonDataList, saveAuthor

def run():
    webtoonDataList = [
        {
            "categoryName": "월",
            "webtoons": [
                {
                    "title": "참교육",
                    "author": "채용택 / 한가람",
                    "rating": 9.89,
                    "imgUrl": "https://~~~~~~"
                },
                {
                    "title": "똑 닮은 딸",
                    "author": "이담",
                    "rating": 9.98,
                    "imgUrl": "https://~~~~~~"
                }
            ]
        }
    ]

    webtoonDataList.clear()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://comic.naver.com/webtoon")
    driver.maximize_window()
    sleep(1)

    categoryLis = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li'
    )

    for categoryLi in categoryLis[1:3]:
        categoryLink = categoryLi.find_element(by=By.CSS_SELECTOR, value="& > a")
        categoryLink.click()
        sleep(0.5)

        webtoonDataOfCategory = {
            "categoryName": categoryLink.text,
            "webtoons": []
        }

        webtoonLis = driver.find_elements(by=By.CSS_SELECTOR, value="#content > div:nth-child(1) > ul > li")
        for webtoonLi in webtoonLis:
            driver.execute_script("arguments[0].scrollIntoView(true);", webtoonLi)
            img = webtoonLi.find_element(by=By.CSS_SELECTOR, value="& > a > div > img")
            imgSrc = img.get_attribute("src")
            title = webtoonLi.find_element(by=By.CSS_SELECTOR, value="& > div > a:nth-of-type(1)")
            titleText = title.text
            author = webtoonLi.find_element(by=By.CSS_SELECTOR, value="& > div .ContentAuthor__author--CTAAP")
            authorText = author.text
            rating = webtoonLi.find_element(by=By.CSS_SELECTOR, value="& > div > div:nth-last-of-type(1) > span > span")
            ratingText = rating.text
            webtoon = {
                "title": titleText,
                "author": authorText,
                "rating": float(ratingText),
                "imgUrl": imgSrc
            }
            webtoonDataOfCategory["webtoons"].append(webtoon)
        webtoonDataList.append(webtoonDataOfCategory)

    print(webtoonDataList)
    saveWebtoonDataList(webtoonDataList)
    saveAuthor(webtoonDataList)









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
        sleep(0.1)

        webtoonTitles = driver.find_elements(by=By.CSS_SELECTOR,
                                             value='#container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul > li > div > a > span > span')

        for webtoonTitle in webtoonTitles:
            print(webtoonTitle.text)

def run3():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://kr.stussy.com/collections/new-arrivals")
    driver.maximize_window()
    sleep(1)

    categoryies = driver.find_elements(
        by = By.CSS_SELECTOR,
        value='#dropdown-menu-1-shop > div > ul > li > a'
    )

    for i in range(len(categoryies)):
        categoryies = driver.find_elements(
            by = By.CSS_SELECTOR,
            value='#dropdown-menu-1-shop > div > ul > li > a'
        )
        categoryName = categoryies[i].text
        print(f"카테고리: {categoryName}")

        driver.execute_script("arguments[0].scrollIntoView(true);", categoryies[i])
        driver.execute_script("arguments[0].click();", categoryies[i])
        sleep(0.1)


        productLis = driver.find_elements(
            by = By.CSS_SELECTOR,
            value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
        )
        # #'#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li:nth-child(4) > div > div'
        for productLi in productLis[:4]:
            productImg = productLi.find_element(by=By.CSS_SELECTOR, value='div > a > div > img')
            productImgSrc = productImg.get_attribute('src')
            productName =  productLi.find_element( by= By.CSS_SELECTOR, value= 'div > div > div:nth-of-type(1)')
            productNameText = productName.text
            productPrice = productLi.find_element(by=By.CSS_SELECTOR, value= 'div > div > div:nth-of-type(2)')
            productPriceText = productPrice.text
            print(f'상품명: {productNameText}, 가격: {productPriceText}, url: {productImgSrc}')

def run4():
    products = []

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://kr.stussy.com/collections/new-arrivals")
    driver.maximize_window()
    sleep(1)

    categoryies = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#dropdown-menu-1-shop > div > ul > li > a'
    )

    for i in range(len(categoryies)):
        categoryies = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#dropdown-menu-1-shop > div > ul > li > a'
        )
        categoryName = categoryies[i].text
        print(f"카테고리: {categoryName}")

        categoryDict = {
            "categoryName": categoryName,
            "productList": []
        }

        driver.execute_script("arguments[0].scrollIntoView(true);", categoryies[i])
        driver.execute_script("arguments[0].click();", categoryies[i])
        sleep(0.1)

        productLis = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
        )
        # #'#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li:nth-child(4) > div > div'
        for productLi in productLis[:4]:
            productImg = productLi.find_element(by=By.CSS_SELECTOR, value='div > a > div > img')
            productImgSrc = productImg.get_attribute('src')
            productName = productLi.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(1)')
            productNameText = productName.text
            productPrice = productLi.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-of-type(2)')
            productPriceText = productPrice.text
            print(f'상품명: {productNameText}, 가격: {productPriceText}, url: {productImgSrc}')
            categoryDict["productList"].append({
                "productName": productNameText,
                "productPrice": productPriceText,
                "productImgSrc": productImgSrc,
            })

        products.append(categoryDict)
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
