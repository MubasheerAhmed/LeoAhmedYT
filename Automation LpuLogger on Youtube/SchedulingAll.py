from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import schedule
import time

global c1
c1 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]/div/div[2]'
global c2
c2 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]/div/div[2]'
global c3
c3 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[2]'
global c4
c4 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]/div/div[2]'
global c5
c5 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]/div/div[2]'


def onehr(var1):

    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    regid.send_keys("YOUR ID")

    password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys("Insert YOUR Password")

    logB = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    tab1 = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

    class3rd =driver.find_element_by_xpath(var1)
    class3rd.click()

    joinB = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(5)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()



    act.send_keys(Keys.ENTER).perform()

# Min amount of time required for attendence is 40 mins per hour on average
# If class joined at 9:05 or 13:05 let it logged in until 10:00 or 14:00 respectively
# so it has to close after 55 mins so you may ender time.sleep(3300) thats 55 mins
# If class joined at 9:03 or 13:03 let it logged in until 10:00 or 14:00 respectively
# so it has to close after 55 mins so you may ender time.sleep(3420) thats 57mins
    time.sleep(3300)
    driver.close()


def twohr(var2):

    driver = webdriver.Chrome()
    driver.get('https://myclass.lpu.in/')

    regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    regid.send_keys("YOUR ID")

    password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys("Insert YOUR Password")

    logB = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

    tab1 = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

    class3rd =driver.find_element_by_xpath(var2)
    class3rd.click()

    joinB = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

    time.sleep(5)

    act = ActionChains(driver)

    for i in range(3):
        act.send_keys(Keys.TAB).perform()

    act.send_keys(Keys.ENTER).perform()

# Min amount of time required for attendence is 40 mins per hour on average
# If class joined at 9:05 or 13:05 let it logged in until 11:00 or 15:00 respectively
# so it has to close after 55 mins so you may ender time.sleep(6900) thats 115 mins
# If class joined at 9:03 or 13:03 let it logged in until 11:00 or 15:00 respectively
# so it has to close after 55 mins so you may ender time.sleep(7020) thats 117 mins
    time.sleep(6900)
    driver.close()

def rest():
    quit()

def timer():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"The Time is: {current_time}")
   
schedule.every(60).seconds.do(timer)
# Strictly mention time in 24Hrs Format

schedule.every().monday.at("09:05").do(twohr, c1)
schedule.every().monday.at("12:03").do(onehr, c2)
schedule.every().monday.at("15:03").do(onehr, c3)
schedule.every().tuesday.at("11:03").do(onehr, c1)
schedule.every().tuesday.at("12:03").do(onehr, c2)
schedule.every().tuesday.at("14:03").do(onehr, c3)
schedule.every().tuesday.at("16:03").do(onehr, c4)
schedule.every().wednesday.at("09:05").do(twohr, c1)
schedule.every().wednesday.at("12:03").do(onehr, c2)
schedule.every().wednesday.at("14:03").do(onehr, c3)
schedule.every().wednesday.at("15:03").do(onehr, c4)
schedule.every().wednesday.at("16:03").do(onehr, c5)
schedule.every().thursday.at("09:05").do(twohr, c1)
schedule.every().thursday.at("14:03").do(onehr, c2)
schedule.every().friday.at("09:05").do(onehr, c1)
schedule.every().friday.at("10:03").do(onehr, c2)
schedule.every().friday.at("13:03").do(twohr, c3)
schedule.every().saturday.at("09:05").do(twohr, c1)
schedule.every().saturday.at("13:03").do(twohr, c2)
schedule.every().saturday.at("16:03").do(onehr, c3)



schedule.every().saturday.at("18:30").do(rest)

while True:
    schedule.run_pending()
    time.sleep(1)
