
from lib2to3.pgen2 import driver
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import configparser
from time import sleep


FILE_PATH : str = os.getcwd()
BROWSER_NAME: str = 'CHROME'


QUIT_BROWSER: bool = True
QUIT_BROWSER: bool = False
EXP_TIME: int = 1800
WAIT_TIME: int = 1800



def init_driver():
        print('Opening Browser........')
        
        if BROWSER_NAME == 'CHROME':
                from selenium.webdriver.chrome.service import Service
                chrome_profile = Options()
                #chrome_profile.add_argument('kiosk-printing')
                chrome_profile.add_argument('start-maximized')
                chrome_profile.add_argument('disable-infobars')
                #chrome_profile.add_argument('--blink-settings=imagesEnabled=false')
                #chrome_profile.add_argument('headless')
                os.makedirs(f'{FILE_PATH}\\User_Data', exist_ok=True)
                #chrome_profile.add_argument(f"user-data-dir={FILE_PATH}\\User_Data")
                chrome_profile.add_argument("--log-level=3")
                print(f'Opening {BROWSER_NAME} Browser........')
                driver = webdriver.Chrome(service =Service(),options=chrome_profile)
        
                
                driver.wait = WebDriverWait(driver, EXP_TIME)
                print(f'{BROWSER_NAME} Browser opened')
        
                return driver


    
def main() -> None:
    driver = init_driver()
    driver.get(URL)
    
      
if __name__ == "__main__":
    main()
