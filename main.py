from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time, pyautogui, random, schedule

user_name = "ENTER IN YOUR E-MAIL HERE"
pw = "ENTER IN YOUR PASSWORD HERE"

#Use 24-hour time format (ex: 23:30 or 1:30)
run_time = "ENTER IN TIME" 

def job():
    driver = webdriver.Chrome("C:\Python34\Lib\site-packages\selenium\chromedriver")
    def logInFB(userName, pw):
        driver.get("http://www.facebook.com")
        user_name_field = driver.find_element_by_name("email")
        user_name_field.send_keys(user_name)
        password_field = driver.find_element_by_name("pass")
        password_field.send_keys(pw)
        pyautogui.press('enter')
        
    def navigateToHappyBirthday():
        driver.get("https://www.facebook.com/events/birthdays")
        time.sleep(3)
        pyautogui.press('esc')


    def random_line():
        lines = open('birthday_wishes.txt').read().splitlines()
        return random.choice(lines)
        
    def write(msg):
        driver.find_element_by_css_selector(".enter_submit.uiTextareaNoResize.uiTextareaAutogrow.uiStreamInlineTextarea.inlineReplyTextArea.mentionsTextarea.textInput").send_keys(msg)
        pyautogui.press('enter')
        time.sleep(5)
#Bot is figuring out how many birthdays there are today.
    amt_of_bdays = len(driver.find_elements_by_css_selector(".enter_submit.uiTextareaNoResize.uiTextareaAutogrow.uiStreamInlineTextarea.inlineReplyTextArea.mentionsTextarea.textInput"))

#Logging into Facebook
    logInFB(user_name,pw)
    navigateToHappyBirthday()

    if amt_of_bdays > 0:
        print("There are " + str(amt_of_bdays) + " birthdays today!")
        #generate random message
        for i in range(0, amt_of_bdays-1):
            msg = random_line()
            write(msg)
    else:
        print("\n\nNo Birthdays today!")
        driver.close()
#Enter in the desired time you'd like to run this script
schedule.every().day.at(run_time).do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)