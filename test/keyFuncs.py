import time
from selenium.webdriver.common.keys import Keys


def mute_on_startup(driver):

    mute_odo_vdo_btns = driver.find_elements_by_class_name('HNeRed')

    for i in range(2):
        mute_odo_vdo_btns[i].click()


def join(driver):

    join_button = driver.find_elements_by_class_name('Fxmcue')
    join_button[0].click()


def mute_on_join(action):

    action.key_down(Keys.CONTROL).send_keys('d').perform()
    time.sleep(1)


def open_atendee_list(driver):
    el = driver.find_elements_by_xpath(
        '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/span/button')

    el[0].click()


def listen_no_of_participants(driver):
    no_of_ptcpnts = driver.find_element_by_class_name('uGOf1d')
    prev_ptc = no_of_ptcpnts.text
    print(f"Participants : {no_of_ptcpnts.text}")

    while True:
        no_of_ptcpnts = driver.find_element_by_class_name('uGOf1d')

        if prev_ptc != no_of_ptcpnts.text:
            prev_ptc = no_of_ptcpnts.text
            print(f"Participants : {no_of_ptcpnts.text}")
