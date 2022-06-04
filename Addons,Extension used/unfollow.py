from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

username1 = input('Your Instagram Login: ') #input('Your Username: ')
password1 = input('Your Instagram Password: ') #input('Your Password: ')

def login(browser):
    browser.get("https://www.instagram.com")
    print('Browser go to Instagram Login Page')
    #browser.maximize_window()
    time.sleep(5)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    #YOUR USERNAME GOES HERE
    username.send_keys(username1)
    #YOUR Password GOES HERE
    password.send_keys(password1)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')\
    .click()
    print('Login Successful')
    time.sleep(5)
    

def Vist_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    print('Browser Loading Account Page')
    time.sleep(sleepy_time)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
    .click()
    print('Go to Followers Tab')
    time.sleep(sleepy_time)
    unfollow_counter = 0
    crash_count = 0
    while True:
        try:
            if unfollow_counter >= 100:
                currentDT = datetime.datetime.now()
                print(currentDT.strftime("%H:%M")," SYSTEM LOG:")
                print('100 Unfollow is Done')  
                print('Program Standby mode ON: 30min')
                time.sleep(1800)
                unfollow_counter = 0
                continue
            pictures = browser.find_element_by_css_selector("[class='sqdOP  L3NKy    _8A5w5    ']")
            pictures.click()
            print('Click on Follower')
            time.sleep(5)
            submit_unfollow = browser.find_element_by_css_selector('[class="aOOlW -Cab_   "]')
            submit_unfollow.click()
            time.sleep(5)
            unfollow_counter += 1
            print("Unfollows: ",unfollow_counter)
        except Exception as e:
            print(e)
            if crash_count >= 5:
                currentDT = datetime.datetime.now()
                print(currentDT.strftime("%H:%M")," SYSTEM LOG:")  
                print('Program Standby mode ON: 30min')
                time.sleep(1800)
                crash_count = 0
                browser.get(url)
                print('Browser Loading Account Page')
                time.sleep(sleepy_time)
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
                .click()
                print('Go to Followers Tab')
                time.sleep(sleepy_time)  
                pass
            crash_count += 1
            currentDT = datetime.datetime.now()
            print(currentDT.strftime("%H:%M")," CRASH LOG:") 
            print('Program Crash: ',crash_count, ' time. Continue in 5 sek.')
            time.sleep(5)
            browser.get(url)
            print('Browser Loading Account Page')
            time.sleep(sleepy_time)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
            .click()
            print('Go to Followers Tab')
            time.sleep(sleepy_time)            
            pass

def main():
    browser = webdriver.Chrome()
    login(browser)

    usernames = [username1]

    while True:
        for username in usernames:
            Vist_Tag(browser, f"https://www.instagram.com/{username}")
        print('Program finish work')    
        break

main()
