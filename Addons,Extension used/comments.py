from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from comment_list import my_list


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
    browser.get('https://www.instagram.com')
    print('Wall loaded')
    time.sleep(5)
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
        .click()
        print('Clicked Not Now')
        time.sleep(sleepy_time)
    except Exception as e:
        print(e)
        print('Button Not Now, is not Detected.')
        pass
    comment_counter = 0
    crash_count = 0
    while True:
        try:
            profil = browser.find_element_by_css_selector("[class='sqdOP yWX7d     _8A5w5   ZIAjV ']")
            time.sleep(2)
            print
            time.sleep(100)
            comment = browser.find_element_by_css_selector('[aria-label="Add a comment…"]')
            time.sleep(2)
            browser.execute_script("window.scrollTo(0, window.scrollY + 1200)")       
            time.sleep(3)
            comment.send_keys(random.choice(my_list))
            time.sleep(3)
            comment.send_keys((Keys.ENTER))
            comment_counter += 1
            print('Comment: ',comment_counter)
            time.sleep(1000)
            #submit_unfollow = browser.find_element_by_css_selector('[class="aOOlW -Cab_   "]')
            #submit_unfollow.click()
        except Exception as e:
            print('\n')
            print(e)
            print('\n')
            if crash_count >= 5:
                break
            crash_count += 1
            print('Program Crash: ',crash_count, ' time. Continue in 60sek.')
            time.sleep(60)            
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
