from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
import arrow


URL = "https://web.whatsapp.com"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Admin\Desktop\\ChromePrfl")
driver = webdriver.Chrome(
    executable_path="C:\\chromedriver.exe", chrome_options=options)
WAIT = WebDriverWait(driver, 50)


def get():
    driver.get(URL)

    WAIT.until(ec.presence_of_element_located((By.CLASS_NAME, "YtmXM")))


def send_message(message, phone):
    url = URL + f"/send?phone={phone}&text={message}"
    driver.get(url)

    element = WAIT.until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, "_13NKt")))
    element[1].click()
    element[1].send_keys(Keys.RETURN)


def attach_image(path):
    element = WAIT.until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#main > footer > div._2BU3P.tm2tP.copyable-area > div._3HQNh._1un-p > div._2jitM > div > span > div._3iTtj > div > ul > li:nth-child(1) > button > input[type=file]")))

    element.send_keys(path)


def get_noti():
    noti_elements = driver.find_elements_by_class_name("_23LrM")

    return noti_elements


'''
https://api.whatsapp.com/send?phone={phoneNumber}&text={text}

'''

if __name__ == "__main__":
    # get()
    # print("breaked!")
    # print(len(get_noti()))
    send_message("Hey!", "917356998597")
    attach_image(r"C:\Users\Admin\Desktop\TimeTable.jpg")
