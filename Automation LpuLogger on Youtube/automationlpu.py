from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://myclass.lpu.in/')

regid = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
regid.send_keys("11804714")

password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys("1aA#pass")

logB = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()

tab1 = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]').click()

class3rd =driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]/div/div[1]')
class3rd.click()

joinB = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a').click()

time.sleep(5)

act = ActionChains(driver)

for i in range(3):
    act.send_keys(Keys.TAB).perform()



act.send_keys(Keys.ENTER).perform()



time.sleep(800)
driver.close()
