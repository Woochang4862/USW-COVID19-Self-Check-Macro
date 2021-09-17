from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import logging
import os
import sys

logger = logging.getLogger()
FORMAT = "[%(asctime)s][%(filename)s:%(lineno)3s - %(funcName)20s()] %(message)s"
logger.setLevel(logging.DEBUG)

def setup_driver():
    try:
        co = Options()
        co.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
        co.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
        if getattr(sys, 'frozen', False):   
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")  
            driver = webdriver.Chrome(chromedriver_path, options=co)
        else:
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(options=co)
        return driver
    except:
        logging.exception("")
        raise Exception("크롬 드라이버를 얻어오는 중 에러 발생")