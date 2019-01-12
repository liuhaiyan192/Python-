from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_elements_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()