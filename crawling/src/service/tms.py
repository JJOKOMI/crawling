from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.repository.tms_repository import selectTms, findBoard


def run():
    title = input("웹툰 제목을 입력하세요:")


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    sleep(2)

    loginId= driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > div > form > table > tbody > tr:nth-child(3) > td > input"
    )

    loginId.send_keys("guswlwldhks")
    sleep(2)

    loginPassword = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input"
    )
    loginPassword.send_keys("26815282")
    sleep(2)

    loginButton = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button"
    )
    loginButton.click()
    sleep(5)

    ncs = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr.hover.pointer > td:nth-child(4)"
    )
    ncs.click()
    sleep(2)

    crawlingButton = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(10) > div"
    )
    driver.execute_script("arguments[0].scrollIntoView();", crawlingButton)
    driver.execute_script("arguments[0].click();", crawlingButton)

    sleep(2)

    boardButton = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > caption > div > div:nth-child(2) > div > a"
    )
    driver.execute_script("arguments[0].scrollIntoView();", boardButton)
    driver.execute_script("arguments[0].click();", boardButton)

    sleep(2)

    BoardInput = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input"
    )
    BoardInput.send_keys("황현지")



    contentInput = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.ck.ck-editor__main > div"
    )
    contentInput.send_keys(values)
    sleep(2)

    okButton = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr.end > td > button"
    )
    driver.execute_script("arguments[0].scrollIntoView();", okButton)
    driver.execute_script("arguments[0].click();", okButton)
    sleep(2)

    selectTms()











