from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import arrow


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Admin\Desktop\\ChromePrfl")
driver = webdriver.Chrome(
    executable_path="C:\\chromedriver.exe", chrome_options=options)


def get():
    driver.get("https://instagram.com")


def get_inbox():
    driver.get("https://www.instagram.com/direct/inbox/")


def login():
    time.sleep(5)
    emailELement = driver.find_element_by_name("username")
    time.sleep(5)
    passwordElement = driver.find_element_by_name("password")
    emailELement.send_keys("aadil.varsh", Keys.TAB)
    passwordElement.send_keys("dream@Instagram21", Keys.ENTER)


def send_msg():
    # prfl_element = driver.find_elements_by_class_name("fDxYl")

    # for element in prfl_element:
    #     if name in element.text:
    #         element.click()
    #         break

    element = driver.find_elements_by_class_name("hjZTB")[-1]

    if "hi" in element.text.lower() or "hello" in element.text.lower():
        time.sleep(5)
        input_element = driver.find_element_by_tag_name("textarea")
        print("got the input!")
        time.sleep(2)
        input_element.send_keys("Heyyyyy!", Keys.RETURN)
        print(f"sent heyy!")
    if "time" in element.text.lower():
        time.sleep(5)
        input_element = driver.find_element_by_tag_name("textarea")
        print("got the input!")
        time.sleep(2)
        input_element.send_keys(
            "It is " + str(arrow.now().format("hh:mm")), Keys.RETURN)
        print(f"sent heyy!")

    # time.sleep(2)
    # time.sleep(3)


def wait_for_msg():
    time.sleep(5)

    print("listening for msgs!!!! ")
    while True:
        not_element = driver.find_elements_by_class_name("Sapc9")

        for element in not_element:
            element.click()
            print("clicked element!")
            send_msg()
            driver.find_elements_by_class_name("_8-yf5 ")[1].click()


'''
_7UhW9   xLCgt      MMzan  KV-D4              fDxYl
_7UhW9   xLCgt      MMzan  KV-D4              fDxYl
_7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB

 _41V_T   Sapc9                 Igw0E     IwRSH      eGOV_         _4EzTm

Igw0E IwRSH YBx95 _4EzTm XfCBB g6RW6
Igw0E IwRSH YBx95 _4EzTm XfCBB g6RW6

 _7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB
 _7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB
'''

if __name__ == "__main__":
    get_inbox()
    wait_for_msg()
