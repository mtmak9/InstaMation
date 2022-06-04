from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

username1 = input('Your Instagram Login: ')
password1 = input('Your Instagram Password: ')
print('\n')
print("Napisz 5 Hashtagow których Bot ma uzyc do pracy: ")
print('\n')
hashtag1 = input("hashtag-1: #")
hashtag2 = input("hashtag-2: #")
hashtag3 = input("hashtag-3: #")
hashtag4 = input("hashtag-4: #")
hashtag5 = input("hashtag-5: #")
#hashtag6 = input("hashtag-6: #")
#hashtag7 = input("hashtag-7: #")
#hashtag8 = input("hashtag-8: #")
print('\n')
print('Program gdy wykona swoja prace przechodzi w stan spoczynku, zalecany czas spoczynku to 3600 sekund - czyli 1h.')
print('\n')
#print('Ale mozesz ustawic dowolny czas wyciszenia dla programu, pamietaj tylko aby podac czas w SEKUNDACH')
#print('1h = 3600s / 30min = 1800s')
#print('\n')
cooldown = int(input("Podaj czas wyciszenia: "))
czas_pracy = round(cooldown/60)
image_max = int(input("Ile Like & Follow, program ma wykonac na 1-Hashtag: \n"))
print('\n')
print('PROCESS LOG:')


def login(browser):
    browser.get("https://www.instagram.com")
    #browser.maximize_window()
    print('Go to Instagram')
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
    time.sleep(5)
    print('Login Successful')

def Vist_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")
    image_count = 0
    like_counter = 0
    follow_counter = 0

    for picture in pictures:
        if image_count >= image_max:
            break
        picture.click()    
        time.sleep(sleepy_time)

        try:
            heart = browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg")
                #Old code for like: ("[aria-label='Like']") 
            heart.click()                
            like_counter += 1
            print('Likes: ',like_counter)
        except Exception as e:
            print(e)
            print("Something went wrong, Like Unsuccessful")
        #Check Instagram limit Pop Up notification    
            try:
                insta_limit = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]")
                insta_limit.click()
                if insta_limit:
                    return True
                    print('Instagram Limit button appear, Standby Mode activate for: ',cooldown,'min')
                    sleep.time(cooldown)
            except Exception:
                pass
        #Check Instagram limit Pop Up notification
            pass
        time.sleep(1)
        try:
            follow = browser.find_element_by_css_selector("div[class='bY2yH']")
            follow.click()
            follow_counter += 1
            print('Follow: ',follow_counter)
        except Exception:
            print('Allready Followed')
        #Check Instagram limit Pop Up notification    
            try:
                insta_limit = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]")
                insta_limit.click()
                if insta_limit:
                    return True
                    print('Instagram Limit button appear, Standby Mode activate for: ',cooldown,'min')
                    sleep.time(cooldown)
            except Exception:
                pass
        #Check Instagram limit Pop Up notification
            pass
        time.sleep(1)
        try:
            cancel = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            cancel.click()
        except Exception:
            pass
        time.sleep(1)
        try:
            close = browser.find_element_by_css_selector("[aria-label='Close']")
            close.click()
        except Exception:
        #Check Instagram limit Pop Up notification    
            try:
                insta_limit = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]")
                insta_limit.click()
                if insta_limit:
                    return True
                    print('Instagram Limit button appear, Standby Mode activate for: ',cooldown,'min')
                    sleep.time(cooldown)
            except Exception:
                pass
        #Check Instagram limit Pop Up notification
        image_count += 1
        time.sleep(sleepy_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [ 
        hashtag1,
        hashtag2,
        hashtag3,
        hashtag4,
        hashtag5,
    ]

    while True:
        for tag in tags:
            Vist_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        currentDT = datetime.datetime.now()
        print(currentDT.strftime("%H:%M")," SYSTEM LOG:")            
        print('Program skonczyl prace, uruchomi sie za minut: ',czas_pracy,'min')
        time.sleep(cooldown)

main()