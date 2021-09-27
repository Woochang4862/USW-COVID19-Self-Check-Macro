from selenium.webdriver.support.ui import *
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import logging
import time

from DriverProvider import setup_driver

logger = logging.getLogger()
FORMAT = "[%(asctime)s][%(filename)s:%(lineno)3s - %(funcName)20s()] %(message)s"
logging.basicConfig(format=FORMAT, filename=f'./log/{time.strftime("%Y-%m-%d")}.log')
logger.setLevel(logging.INFO)

def macro(driver, no, pw, name):
    wait = WebDriverWait(driver, 10)

    driver.get("https://portal.suwon.ac.kr/enview/");

    try:
        driver.switch_to.frame("mainFrame")
    except:
        logging.exception("")

    try:
        input_id = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@name="userId"]'))
        )[0]
        input_id.send_keys(no)

        input_pw = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@name="pwd"]'))
        )[0]
        input_pw.send_keys(pw)

        login_button = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="mainbtn_login"]'))
        )[0]
        login_button.click()
    except:
        logging.exception("")

    try:
        info_button = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@alt="종합정보시스템"]'))
        )[0]
        info_button.click()
    except:
        logging.exception("")

    try:
        driver.switch_to.window(driver.window_handles[1])
        
        dorm_item = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="treeMenu_label_44"]'))
        )
        dorm_item.click()

        self_check_item = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="treeMenu_label_45"]'))
        )
        self_check_item.click()
    except:
        logging.exception("")

    try:
        iframe = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="windowContainer1_subWindow1_iframe"]'))
        )
        driver.switch_to.frame(iframe)

        input_no = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="eno"]'))
        )
        input_no.send_keys(no)

        input_name = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="enm"]'))
        )
        input_name.send_keys(name)

        input_trigger = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="trigger32_row"]'))
        )
        input_trigger.click()

        driver.implicitly_wait(3)

        radio_btns = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="w2radio_input"]'))
        )
        for i, radio_btn in enumerate(radio_btns):
            if i%2 == 0:
                radio_btn.click()

        submit_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="saBtn_row"]'))
        )
        submit_button.click()

        driver.implicitly_wait(3)
    except:
        logging.exception("")

    
if __name__ == "__main__":
    try:
        driver = setup_driver()
        with open("info.txt","rt", encoding='UTF8') as f:
            lines = f.readlines()
            no = lines[0].strip()
            pw = lines[1].strip()
            name = lines[2].strip()
            f.close()
        macro(driver, no, pw, name)
        for window_handle in driver.window_handles:
            driver.switch_to.window(window_handle)
            driver.close()
    except:
        logging.exception("")    