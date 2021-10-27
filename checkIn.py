import time
import datetime
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='D:/truc/Python/tool/CheckIn/chromedriver.exe')
driver.set_window_size(1500, 800)
driver.get('url')

#open txt file
f = open('D:\\truc\\Python\\tool\\CheckIn\\account.txt', 'r')

#remove \n
rez = []
for x in f:
    rez.append(x.replace("\n", ""))
   
#get line data in txt file
#array
username = str(rez[0])
password = str(rez[1])

#get id
driver.find_element_by_id("login").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
#get full xpath
driver.find_element_by_xpath('/html/body/div/main/section/div/div/div/div/div[2]/section/form/div/div[3]/button').click()
time.sleep(5)
#get class name
# driver.find_element_by_class_name('full').click()
# time.sleep(20)
# driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li/div/div[4]/div[2]/div[2]/a[4]').click()
# time.sleep(5)
#get link
#driver.find_element_by_link_text("url").click()

timeCheckIn = '08:14:00'
timeCheckOut = '17:30:00'

def check_in():
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/a').click()

def check_out():
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/a').click()
    
while True:
    if datetime.now().strftime('%H:%M:%S') <= timeCheckIn:
        check_in()
        print("check in success: "+  datetime.now().strftime('%H:%M:%S'))
        time.sleep(60)
        continue
    elif datetime.now().strftime('%H:%M:%S') <= timeCheckOut :
        print("waiting time: " +  datetime.now().strftime('%H:%M:%S'))
        time.sleep(60)
        continue
    else:
        check_out()
        print("check out success: "+  datetime.now().strftime('%H:%M:%S'))
        break
    


