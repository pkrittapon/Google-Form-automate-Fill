from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

browser = webdriver.Chrome()
browser.get('https://forms.gle/GUcqmpu7zmQ8AR7H9')

time.sleep(3)

clickLogin = browser.find_element(By.XPATH,'//*[@id="identifierId"]')
clickLogin.send_keys("example@gmail.com") # USERNAME

clicknext = browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
clicknext.click()
time.sleep(3)
clickpassword = browser.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
clickpassword.send_keys("password") # PASSWORD

clicklogin = browser.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span')
clicklogin.click()

time.sleep(25)
click1 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
click1.click()

click2 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label') 
click2.click()

click2 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/label')
click2.click()

time.sleep(1)

click3 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
click3.click()



for _ in range(4):
    pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

time.sleep(3)

click4 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
click4.click()

time.sleep(3)

click5 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
click5.send_keys("asdfhjkl")

click6 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
click6.send_keys(
"""paragraph
asfasdljasdl
asdflksajfj

asdfasjdfladf""")
time.sleep(1)
click7 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
click7.click()
for _ in range(2):
    pyautogui.keyDown("left"); pyautogui.keyUp("left")

click7.send_keys("01162023")
time.sleep(1)

click8 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
click8.click()
click8.send_keys("12")
click9 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
click9.click()
click9.send_keys("02")

time.sleep(3)

click10 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
click10.click()

time.sleep(3)

click11 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div')
click11.click()

click12 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div')
click12.click()

click13 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')
click13.click()

click14 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/label[1]/div/div/div[2]')
click14.click()

click15 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/label[3]/div/div/div[2]')
click15.click()

click16 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/label[2]/div/div/div[2]')
click16.click()

click17 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/label[4]/div/div/div[2]')
click17.click()

click7 = browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
click7.click()

time.sleep(5)

browser.close()
