from selenium import webdriver
import time

user_input = input("name of file: ")

chrome_browser = webdriver.Chrome(executable_path='D:\Python Projects\chromedriver')
chrome_browser.get('https://github.com/login')

text_input = chrome_browser.find_element_by_xpath('//input[@class="form-control input-block"]')
text_input.send_keys('achyutha.nr10@gmail.com')
time.sleep(10)

new_rep = chrome_browser.find_element_by_xpath('//a[@class="btn btn-sm btn-primary text-white"]')
new_rep.click()
time.sleep(1)

new_rep_name = chrome_browser.find_element_by_xpath('//input[@class="form-control js-repo-name js-repo-name-auto-check short"]')
new_rep_name.send_keys(user_input)

chekbox = chrome_browser.find_element_by_xpath('//input[@id="repository_auto_init"]')
chekbox.click()

create = chrome_browser.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
time.sleep(1)
create.click()
time.sleep(1)

upload_but = chrome_browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/div[4]/div[2]/a[1]')
time.sleep(1)
upload_but.click()