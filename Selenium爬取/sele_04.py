from selenium import webdriver
import time

# browser = webdriver.Chrome()
# # browser.implicitly_wait(10)
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# # browser.add_cookie({'Name':'Bob '})
# print(browser.get_cookies())
# browser.close()
# browser.find_element_by_class_name('')

"""
    自动化控制前进或后退网址
"""
browser = webdriver.Chrome()
url1 = 'http://www.baidu.com'
url2 = 'https://www.zhihu.com/explore'
url3 = 'https://www.python.org/'
browser.get(url1)
browser.execute_script('window.open()')
print(browser.switch_to_window(browser.window_handles[1]))
browser.switch_to_window(browser.window_handles[1])
browser.get(url2)
time.sleep(2)
print(browser.switch_to_window(browser.window_handles[0]))
browser.switch_to_window(browser.window_handles[0])
browser.get(url3)

# browser.get(url2)
# browser.get(url3)
# browser.back()
# # 睡眠2秒
# time.sleep(2)
# browser.forward()
# browser.close()