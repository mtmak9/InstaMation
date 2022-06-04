from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random
from tkinter import *
from tkinter import messagebox
import os
from threading import Thread
import subprocess

    #----------------ABOUT DEVELOPER---------------#
    #    Program is created by Michal Makarewicz   #
    # Application and script is Licenced Free, you #
    # Can Copy,modify and do what you need with it #
    # Instagram Bot is Full Invisible until you    #
    # prepare your chromedriver, check in google   #
    # how to do it. As in ChromeBrowser Driver is  #
    # Code where Instagram can see is Selenium use #
    #----------------------------------------------#
#----------------TKINTER GUI-------------------#
tk=Tk()
tk.title("InstaMation v2.7")
tk.geometry("400x450")
tk.iconbitmap('data/Insta_icon.ico')
tk.configure(bg="#ff8100")
tklogin = StringVar()
tkpassword = StringVar()
tkcooldown = IntVar()
tklikes = IntVar()
tkunfollow = IntVar()
tkhashtag1 = StringVar()
tkhashtag2 = StringVar()
tkhashtag3 = StringVar()
tkhashtag4 = StringVar()
tkhashtag5 = StringVar()
tkcomment_chance = IntVar()
like_counter = 0
follow_counter = 0
comment_counter = 0

#running = True
#---CHECKBOXES---#
tkcomments_active = IntVar(value=0)
C1 = Checkbutton(tk, text="Comment Posts", bg="#ff8100", activebackground='#ff8100', variable=tkcomments_active).grid(column=0,row=11, sticky=W)
tkunfollow_active = IntVar(value=0)
C2 = Checkbutton(tk, text="Unfollow",bg="#ff8100", activebackground='#ff8100', variable=tkunfollow_active).grid(column=1,row=11, sticky=W)
#----------------SYSTEM CONSOLE LOG-----------------#
#print(sys.version)
#print(sys.executable)
random_time = random.randint(3,8)
print('\n')
print('PROCESS LOG:')
#----------------CLEAN BUTTON-----------------------#
def clean_data():
    subprocess.call([r'ChromeTaskKill.bat'])
    #if os.path.isfile('save.txt'):
    #    with open('save.txt','a') as f:
    #        f.truncate(0)
#----------------LOAD BUTTON------------------------#
def load_data():
    #LOAD SETTINGS FROM SAVE.TXT
    if os.path.isfile('save.txt'):
        with open('save.txt','r') as f:
            all_lines = f.read().split(',')
            tklogin.set(all_lines[0])
            tkpassword.set(all_lines[1])
            tkcooldown.set(all_lines[2])
            tklikes.set(all_lines[3])
            tkunfollow.set(all_lines[4])
            tkhashtag1.set(all_lines[5])
            tkhashtag2.set(all_lines[6])
            tkhashtag3.set(all_lines[7])
            tkhashtag4.set(all_lines[8])
            tkhashtag5.set(all_lines[9])
            tkcomments_active.set(all_lines[10])
            tkunfollow_active.set(all_lines[11])
            tkcomment_chance.set(all_lines[12])
    #tkinter.messagebox.showinfo(title='Loading', message='Settings successfully loaded')
#----------------SAVE BUTTON------------------------#
def save_data():
    atklogin = tklogin.get()
    atkpassword = tkpassword.get()
    atkcooldown = tkcooldown.get()
    atklikes = tklikes.get()
    atkunfollow = tkunfollow.get()
    atkhashtag1 = tkhashtag1.get()
    atkhashtag2 = tkhashtag2.get()
    atkhashtag3 = tkhashtag3.get()
    atkhashtag4 = tkhashtag4.get()
    atkhashtag5 = tkhashtag5.get()
    atkcomments_active = tkcomments_active.get()
    atkunfollow_active = tkunfollow_active.get()
    atkcomment_chance = tkcomment_chance.get()
    #Error message
    if(atklogin=='' or atkpassword=='' or atkcooldown=='' or atklikes=='' or atkunfollow=='' or atkhashtag1=='' or atkhashtag2=='' or atkhashtag3=='' or atkhashtag4=='' or atkhashtag5=='' or atkcomment_chance==''):
        print('Error')
        messagebox.showerror('error','somewhere is missing requied value...')

    elif(atkcooldown <= 1):
        print('Error 2')
        messagebox.showerror('error','cooldown time is too low, please select higher limit, recommended: 60+ minutes ')
        tkcooldown.set('')
    elif(atkcomment_chance <= 1):
        print('Error 2')
        messagebox.showerror('error','Comment chance need to be higher than 1, even if you not set active comments option ')
        tkcomment_chance.set('')
    else:
        result = messagebox.askquestion("Saving","Are you sure you want to Save/Overwrite the current data")
        if(result=='yes'):
            print('You have successfully save your settings!')
        #SAVE LIST TO TXT
            pList = [atklogin,atkpassword,atkcooldown,atklikes,atkunfollow,atkhashtag1,atkhashtag2,atkhashtag3,atkhashtag4,atkhashtag5,atkcomments_active,atkunfollow_active,atkcomment_chance]
            with open("save.txt", 'w') as f:
                f.truncate(0)
                f.write(','.join(map(str,pList)))
    #LABELS
#----------------LOGIN PROCESS----------------------#
def login(browser):
    userlogin = tklogin.get()
    userpass = tkpassword.get()
    unfollowers = tkunfollow.get()
    browser.get("https://www.instagram.com")
    #browser.maximize_window()
    print('Go to Instagram')
    time.sleep(3)
    try:
        accept_cookies = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept_cookies.click()
    except:
        pass
    time.sleep(5)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    
    #YOUR USERNAME GOES HERE
    username.send_keys(userlogin)
    #YOUR Password GOES HERE
    password.send_keys(userpass)
    time.sleep(3)
    login_instagram = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    login_instagram.click()
    time.sleep(5)
    print('Login Successful')
#----------------COMMENTS LIST----------------------#
def comment_list():
    os.system('comments_list.txt')
#----------------UPDATE DRIVER----------------------#
def update_driver():
    print('Checking for new Webdriver...')
    print('Webdriver Update Complete...')
#---------------TEST--------------------------------#
def test():
    all_lines = open("comments_list.txt", "r").read().splitlines()
    names_list = [name for name in all_lines if name]
    random.shuffle(names_list)
    print(random.choice(names_list))

#---------------FOLLOW & LIKES----------------------#
def Follow_Likes(browser, url):
    image_max = tklikes.get()
    cooldown1 = tkcooldown.get()
    comments_status = tkcomments_active.get()
    unfollow_active = tkunfollow_active.get()
    x = tkcomment_chance.get()
    czas_pracy = round(cooldown1*60)
    browser.get(url)
    time.sleep(5)
    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")
    #----------------------------
    image_count = 0
    global like_counter
    global follow_counter
    global comment_counter
    #tk.destroy()    
    for picture in pictures:
        if image_count >= image_max:
            break
        picture.click()    
        time.sleep(3)    
        try:
            heart = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
            #-----Old code for like: ("[aria-label='Like']")------# class="_8-yf5 "
            heart.click()             
            like_counter += 1
            print('Likes: ',like_counter)
            time.sleep(random_time)
        except:
            print('Error: Heart')
            time.sleep(random_time)
            pass
    #-----------Check Instagram limit Pop Up notification--------------------------------------------------------#    
            #try:
            #    insta_limit1 = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/button[2]")
            #    insta_limit1.click()
            #    time.sleep(random_time)
            #    if insta_limit1: 
            #        return True
            #        print('Instagram Limit button appear, Standby Mode activate for: ',cooldown1,'min')
            #        time.sleep(cooldown1)
            #except Exception:
            #    time.sleep(random_time)
            #    pass
    #-----------Check Instagram limit Pop Up notification--------------------------------------------------------#
        try:
            if unfollow_active == 1:
                follow = browser.find_element_by_css_selector("div[class='bY2yH']")
                follow.click()
                time.sleep(random_time)
                follow_counter += 1
                print('Follow:',follow_counter)
            if unfollow_active == 0:
                pass
        except:
            print('Error: Follow')
            pass
    #-----------Check Instagram limit Pop Up notification--------------------------------------------------------#     
        try:
            if unfollow_active == 1:
                cancel = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
                cancel.click()
                print('Allready Followed')
                follow_counter -= 1
                time.sleep(random_time)
            if unfollow_active == 0:
                pass
        except:
            print('Error: Cancel')
            pass
        time.sleep(2)
    #----------------COMMENTS OPTION---------------------------------------------------------------------------#      
        try:
            if comments_status == 1:
                #--------IMPORT COMMENT LIST
                all_lines = open("comments_list.txt", "r").read().splitlines()
                names_list = [name for name in all_lines if name]
                dice = random.randint(1,x)
                #print('wylosowano: ',dice)
                if dice == x:
                    click_comment = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > div > svg')
                    click_comment.click()
                    time.sleep(3)
                    single_comment = random.choice(names_list)
                    comment = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
                    comment.send_keys(single_comment)
                    post_button = browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button')
                    post_button.click()
                    print('Send comment: ', single_comment)
                    random.shuffle(names_list)
                    comment_counter += 1
                    print('Comments:',comment_counter)
                    time.sleep(3)
        except Exception as e:
            print(e)
            pass
    #-------------------------------------------------------------------------------------------------------------#                
        try:
            close = browser.find_element_by_css_selector("[aria-label='Close']")
            close.click()
            time.sleep(random_time)
        except:
            print('Error: Close')
            time.sleep(random_time)
            pass
        image_count += 1
        time.sleep(random_time)
#-----------------UNFOLLOW--------------------------#
def Unfollow_master(browser, url):
    cooldown = tkcooldown.get()
    czas_pracy = round(cooldown*60)
    unfollowers = tkunfollow.get()
    browser.get(url)
    print('Browser Loading Account Page')
    time.sleep(random_time)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
    .click()
    print('Go to Followers Tab')
    time.sleep(random_time)
    unfollow_counter = 0
    crash_count = 0      
    while True:
        try:
            if unfollow_counter >= unfollowers:
                currentDT = datetime.datetime.now()
                print(currentDT.strftime("%H:%M")," SYSTEM LOG:")
                print(unfollowers,' Unfollow is Done')  
                unfollow_counter = 0
                break
            click_unfollow_profil = browser.find_element_by_css_selector("[class='sqdOP  L3NKy    _8A5w5    ']")
            click_unfollow_profil.click()
            time.sleep(random_time)
            submit_unfollow = browser.find_element_by_css_selector("[class='aOOlW -Cab_   ']")
            submit_unfollow.click()
            time.sleep(random_time)
            unfollow_counter += 1
            print("Unfollows: ",unfollow_counter)
        # -----------WHEN PROGRAM CRASH 5 TIMES-------------------#            
        except Exception as e:
            print('Crash Error: Unfollow')
            if crash_count >= 10:
                currentDT = datetime.datetime.now()
                print(currentDT.strftime("%H:%M")," CRASH LOG:")
                print('Program Crash 10 times.')  
                print('Standby mode ON: 10min')
                time.sleep(600)
                crash_count = 0
                browser.get(url)
                print('Browser Loading Account Page')
                time.sleep(random_time)
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
                .click()
                print('Go to Followers Tab')
                time.sleep(random_time)
                print('Program reset Loop, and continue Work.')  
                continue            
            crash_count += 1
            currentDT = datetime.datetime.now()
            print(currentDT.strftime("%H:%M")," CRASH LOG: ")
            print('Program Crash: ',crash_count, ' time. Continue in 5 sek.')
            time.sleep(random_time)
            browser.get(url)
            print('Browser Loading Account Page')
            time.sleep(random_time)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
            .click()
            print('Go to Followers Tab')
            time.sleep(random_time)
            print('Program finish Loop after Crash, pass process to Begin UnFollow While Loop.')            
            pass
#------------START/STOP BUTTONS---------------------#
def button_start():
        #global running  #create global
        running = True
        # Create new thread
        t = Thread(target = main)
        # Start new thread
        t.start()
#-----------------STOP------------------------------#
#def button_stop(browser):
#    global running  #create global
#    running = False
#    try:
#        browser.driver.close()
#        time.sleep(1)
#        tk.destroy()
#    except:
#        print('Can not Close program this time.')
#        pass
#---------------MAIN FUNCTION-----------------------#
def main():
    username1 = tklogin.get()
    cooldown2 = tkcooldown.get()
    czas_pracy2 = round(cooldown2*60)
    hashtag1 = tkhashtag1.get()
    hashtag2 = tkhashtag2.get()
    hashtag3 = tkhashtag3.get()
    hashtag4 = tkhashtag4.get()
    hashtag5 = tkhashtag5.get()
    check_likes = tklikes.get()
    unfollow_active = tkunfollow_active.get() 
    options = webdriver.ChromeOptions()
    #options.add_argument("--user-data-dir=Chrome_Profile\\" + Chrome_username)
    # USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
    #options.add_argument("--profile-directory=Default")
    options.add_argument('--lang=en')
    #options.add_argument("--start-maximized")
    #browser = webdriver.Chrome(executable_path=r"data/chromedriver.exe")
    browser = webdriver.Chrome()
    #print('Check likes: ',check_likes)
    #print('unfollow Active: ',unfollow_active)
    if check_likes == 0 and unfollow_active == 0:
        print('Error, missing Follow&Likes or Unfollow Requied value for working program correctly.')
        messagebox.showerror('error','somewhere is missing requied value...')
        browser.close()
        browser.quit()
        os.system("pause")
    #browser.minimize_window()
    #print('Browser has been maximized')
    tk.destroy()
    login(browser)
    usernames = [username1]
    tags = [ 
        hashtag1,
        hashtag2,
        hashtag3,
        hashtag4,
        hashtag5,
    ]    
    while True:    
        while True:
            if check_likes == 0:
                print('Skipe Like&Follow, process has been Disabled')
                break
            for tag in tags:
                Follow_Likes(browser, f"https://www.instagram.com/explore/tags/{tag}")
            currentDT = datetime.datetime.now()
            print(currentDT.strftime("%H:%M")," SYSTEM LOG:")            
            print('Program skonczyl Follow & Likes proces, uruchomi sie za: ',cooldown2,'min')
            time.sleep(czas_pracy2)
            break
        while True:
            if unfollow_active == 0:
                print('Skip Unfollow, process has been Disabled')
                break
            for username in usernames:
                Unfollow_master(browser, f"https://www.instagram.com/{username}")
            currentDT = datetime.datetime.now()
            print(currentDT.strftime("%H:%M")," SYSTEM LOG:")
            print('Program skonczyl Unfollow proces, uruchomi sie za: ',cooldown2,'min')    
            time.sleep(czas_pracy2)
            break
    else:
        print('Program has been Crash...')
        print('Something went wrong, Program return False...')        
#-----------TKINTER LABELS--------------------------#
login_label = Label(tk,text="Login:", bg="#ff8100")
login_label.grid(column=0, row=0, sticky=E, pady=1, padx=1)
entry_login = Entry(tk,textvariable=tklogin)
entry_login.grid(column=1,row=0, pady=1, padx=1)
    #PASSWORD   
password_label = Label(tk,text="Password:", bg="#ff8100")
password_label.grid(column=0, row=1, sticky=E, pady=1, padx=1)
entry_password = Entry(tk,show='*',textvariable=tkpassword)
entry_password.grid(column=1,row=1, pady=1, padx=1)
    #COOLDOWN
cooldown_label = Label(tk,text="Cooldown:", bg="#ff8100")
cooldown_label.grid(column=0, row=2, sticky=E, pady=1, padx=1)
entry_cooldown = Entry(tk,textvariable=tkcooldown)
entry_cooldown.grid(column=1,row=2, pady=1, padx=1)
    #COOLDOWN MINUTES
min_label = Label(tk,text="(minutes)", bg="#ff8100")
min_label.grid(column=2, row=2, sticky=W)
    #FOLLOW&LIKES
follow_label = Label(tk,text="Follow & Like:", bg="#ff8100")
follow_label.grid(column=0, row=3, sticky=E, pady=1, padx=1)
entry_follow = Entry(tk,textvariable=tklikes)
entry_follow.grid(column=1,row=3, pady=1, padx=1)
    #FOLLOW_LIKE LABEL
#follow_label2 = Label(tk,text="", bg="#ff8100")
#follow_label2.grid(column=2, row=3, sticky=W)
    #UNFOLLOWS
unfollow_label = Label(tk,text="Unfollow:", bg="#ff8100")
unfollow_label.grid(column=0, row=4, sticky=E, pady=1, padx=1)
entry_unfollow = Entry(tk,textvariable=tkunfollow)
entry_unfollow.grid(column=1,row=4, pady=1, padx=1)
    #HASHTAG1
hashtag1_label = Label(tk,text="Hashtag 1:", bg="#ff8100")
hashtag1_label.grid(column=0, row=5, sticky=E, pady=1, padx=1)
entry_hashtag1 = Entry(tk,textvariable=tkhashtag1)
entry_hashtag1.grid(column=1,row=5, pady=1, padx=1)
    #HASHTAG2
hashtag2_label = Label(tk,text="Hashtag 2:", bg="#ff8100")
hashtag2_label.grid(column=0, row=6, sticky=E, pady=1, padx=1)
entry_hashtag2 = Entry(tk,textvariable=tkhashtag2)
entry_hashtag2.grid(column=1,row=6, pady=1, padx=1)
    #HASHTAG3
hashtag3_label = Label(tk,text="Hashtag 3:", bg="#ff8100")
hashtag3_label.grid(column=0, row=7, sticky=E, pady=1, padx=1)
entry_hashtag3 = Entry(tk,textvariable=tkhashtag3)
entry_hashtag3.grid(column=1,row=7, pady=1, padx=1)
    #HASHTAG4
hashtag4_label = Label(tk,text="Hashtag 4:", bg="#ff8100")
hashtag4_label.grid(column=0, row=8, sticky=E, pady=1, padx=1)
entry_hashtag4 = Entry(tk,textvariable=tkhashtag4)
entry_hashtag4.grid(column=1,row=8, pady=1, padx=1)
    #HASHTAG5
hashtag5_label = Label(tk,text="Hashtag 5:", bg="#ff8100")
hashtag5_label.grid(column=0, row=9, sticky=E, pady=1, padx=1)
entry_hashtag5 = Entry(tk,textvariable=tkhashtag5)
entry_hashtag5.grid(column=1,row=9, pady=1, padx=1)
    #SEPARATOR
#separator= Label(tk,text="                  ", bg="#ff8100")
#separator.grid(column=1, row=10)  
    #SAVE BUTTON
save_button= Button(tk,text="    Save    ", font=('Calibri',10), bg="#97DB98", borderwidth=2, command=save_data)
save_button.grid(column=2, row=13, padx=10, pady=10)
    #LOAD BUTTON
load_button= Button(tk,text="    Load    ", font=('Calibri',10), bg="#FFFF99", borderwidth=2, command=load_data)
load_button.grid(column=0, row=13, padx=10, pady=10)
    #CLEAR BUTTON
clean_button= Button(tk,text="Kill chrome process", font=('Calibri',10), bg="#78abf2", command=clean_data)
clean_button.grid(column=1, row=13, padx=10, pady=10)
    #START BUTTON
start_button= Button(tk,text="            Start           ", font=('Calibri',10,'bold'), bg="#00FF00", borderwidth=3, command=main)
start_button.grid(column=1, row=12, padx=10, pady=10)
    #STOP BUTTON
#stop_button = Button(tk, text="Stop", bg="#f93939", command=button_stop)
#stop_button.grid(column=0, row=11)
    #OPEN COMMENT LIST BUTTON
list_button= Button(tk,text="Comments", font=('Calibri',8), bg="#fd76ba", command=comment_list)
list_button.grid(column=0, row=12, padx=10, pady=10)
    #UPDATE CHROMEDRIVER
list_button= Button(tk,text="   Update   ", foreground='white', font=('Calibri',8), bg="#182B6F", command=update_driver)
list_button.grid(column=2, row=12, padx=10, pady=10)
    #TEST---
#test= Button(tk,text="    TEST BUTTON        ", font=('Calibri',8), bg="white", command=test)
#test.grid(column=1, row=16, padx=10, pady=10)
    #COMMENT CHANCE
comment_chance_label = Label(tk,text="Comment chance:", bg="#ff8100")
comment_chance_label.grid(column=0, row=10, sticky=E, pady=1, padx=1)
comment_chance_entry = Entry(tk,textvariable=tkcomment_chance)
comment_chance_entry.grid(column=1,row=10, pady=1, padx=1)
comment_label = Label(tk,text="(1 = 100%, 10 = 10%)", bg="#ff8100")
comment_label.grid(column=2, row=10, sticky=W)
    #STOPKA
#stopka = Label(tk,text="   ", bg="#ff8100")
#stopka.grid(column=1, row=18)
stopka = Label(tk,text="Created by", font=('Calibri',8), bg="#ff8100")
stopka.grid(column=1, row=19)
stopka = Label(tk,text="M. Makarewicz®", font=('Calibri',8), bg="#ff8100")
stopka.grid(column=1, row=20)
tk.mainloop()