from  drivers import init_driver, FILE_PATH
import re
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
pattern = r"\d{5}-[A-Z]+-\d{3}"
while(True):
    PIN = input("Enter SAMPLE PIN: ")
    PIN = PIN.replace(" ", "")
    PIN = PIN.upper()
    match = re.match(pattern, PIN)
    print(PIN)
    if match:
        print("PIN Pattern found!")
        PIN = PIN[:-1]
        print(f"PIN Series {PIN}")
        break
    else:
        print("PIN Pattern No match.Try again.....")


TEST_URL: str = f"file://{FILE_PATH}/SFDBK.html"
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
        while(True):
            box = sb_fdback.wait.until(EC.alert_is_present())
            box = sb_fdback.switch_to.alert
            print(box.text)
            if "OTP sent to the mobile number" in box.text:
                box.accept()
                break
            else:
                print("Try again...")
                box.accept()
        #sleep(7)
        sleep(15)
        sub = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/form/table/tbody/tr[1]/td[2]')))
        sub = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/form/div[5]/button')))
        sub = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/form/div[3]/table/tbody/tr[1]/th[2]')))
        box = sb_fdback.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="feedbackcontainer"]/form/div[3]/table/tbody')))
        #stars = box.find_element_by_css_selector("[title^='Excellent']")
        #rating = box.find_elements(by=By.CLASS_NAME, value='rating')
        sleep(5)
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
        print("Enter Next PIN")
    
    
if __name__ == "__main__":
    main()
