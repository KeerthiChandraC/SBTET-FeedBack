
from time import time
from  drivers import init_driver, FILE_PATH


from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
import configparser
from time import sleep

PIN = '22087-EC-0'


TEST_URL: str = f"file://{FILE_PATH}/myurl.html"
URL: str =  "https://www.sbtet.telangana.gov.in/index.html#!/index/StudentFeedback"
FB_URL : str = "https://www.sbtet.telangana.gov.in/API/api/PreExamination/GenerateOtpForFeedback?FeedbackId=3&Pin=21087-EC-059"
FB_PIN_URL : str = "https://www.sbtet.telangana.gov.in/API/api/PreExamination/getFacultyData?FeedbackId=3&Otp=5E5214&Pin=21087-EC-059"


def main()-> None:
    sb_fdback = init_driver()
    sb_fdback.get(URL)
    while(True):
        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/div[1]/div/div/div[1]/div/select')))
        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/div[1]/div/div/div[2]/div/input')))
        sleep(2)
        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/div[1]/div/div/div[1]/div/select')))
        box.send_keys( Keys.ARROW_DOWN)
        mySelect = Select(box)

       # mySelect.send_keys( Keys.ARROW_DOWN)

        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/div[1]/div/div/div[2]/div/input')))
        
        box.clear()
        box.send_keys(f"{PIN}")

        box = sb_fdback.wait.until(EC.alert_is_present())
        box = sb_fdback.switch_to.alert
        print(box.text)
        #sleep(7)
        box.accept()
        sleep(15)
        sub = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/ui-view/div/div[2]/ui-view/div[1]/div[1]/form/div[3]/table/tbody/tr[12]/td[2]')))
        sub = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/ui-view/div/div[2]/ui-view/div[1]/div[1]/form/div[5]/button')))
        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/form/div[3]/table/tbody')))
        #stars = box.find_element_by_css_selector("[title^='Excellent']")
        #rating = box.find_elements(by=By.CLASS_NAME, value='rating')
        sleep(3)
        stars = box.find_elements(by=By.CSS_SELECTOR, value="[title^='Excellent']")
        print("found stars...")
        #stars = box.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value="[title^='Excellent']"))
        print("clicking satrs...")
        for star in stars:
            star.click()
        print("Clik sumbit")
        #sub.click()
        box = sb_fdback.wait.until(EC.alert_is_present())
        box = sb_fdback.switch_to.alert
        print(box.text)
        box.accept()
        sleep(5)
    
    
if __name__ == "__main__":
    main()
