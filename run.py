

from common import method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = test_data.data["url"]
username = test_data.data.get("username")
password = test_data.data.get("password")
key = test_data.data.get("key")
print(url, username, password, key)

num = method.search_fun(driver,url,username,password,key)
if key in num:
    print("搜索用例通过！")
else:
    print("搜索失败")