
# from python import lesson_01   #导入
# def execute_fun(filename,sheetname):
#     cases = lesson_01.read_data(filename, sheetname)     #调用读取数据
#     for case in cases:
#         case_id = case.get("case_id")
#         url = case.get("url")   # 获取url地址
#         data = case["data"]    #获取测试参数
#         data = eval(data)   #去掉引号
#         expected_result = case.get("expected_result")
#         expected_result = eval(expected_result)      #去掉引号
#         expected_msg = expected_result.get("msg")
#         real_result = lesson_01.api_func(url_api=url, data_api=data)  #调用接口发送的参数
#         real_msg = real_result.get("msg")
#         print("真实执行结果：{}".format(real_msg))
#         print("预期执行结果：{}".format(expected_msg))
#         if real_msg == expected_msg:
#             final_result = "Passed"
#             print("第{}条测试用例执行通过".format(case_id))
#         else:
#             final_result = "Failed"
#             print("第{}条测试用例执行不通过".format(case_id))
#         print("*" * 20)
#         lesson_01.write_result(filename, sheetname, final_result, case_id+1, 8)  #调用写入结果的函数
# execute_fun("test_case_api.xlsx", "login")

#
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://baidu.com")
# driver.maximize_window()
# driver.get("https://taobao.com")
# driver.back()   #返回上一个页面
# driver.forward() #前进一个页面
# driver.refresh()  #刷新页面
# driver.time()  #休眠时间
#关闭浏览器
#close()关闭当前窗口，不会退出浏览器
#quit   关闭浏览器，清除缓存

#/html/body/div/div/div[1]/a/small
#//*[@id="username"]

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
page_title = driver.title
if page_title =='柠檬ERP':
    print("这个页面的标题是：{}".format(page_title))
else:
    print("这个用例不通过")


driver.find_element_by_id('username').send_keys('test123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id('btnSubmit').click()
page_name = driver.find_element_by_xpath("//p").text
if page_name =='测试用户':
    print("这个登录名是：{}".format(page_name))
else:
    print("这个用例不通过")

driver.find_element_by_xpath('//span[text()="零售出库"]').click()
id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
id_frame = id_li + '-frame'
# driver.switch_to.frame(id_frame)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(id_frame)))
driver.find_element_by_id('searchNumber').send_keys('841')
driver.find_element_by_id('searchBtn').click()
time.sleep(1)
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-2']//td[@field='number']/div").text
if "841" in num:
    print("搜索用例通过！")
else:
    print("搜索失败")

def open_url(driver, url):
    driver.get(url)
    driver.maximize_window()

def login_func(driver, username, password,):
    driver.find_element_by_id(username).send_keys(username)
    driver.find_element_by_id(password).send_keys(password)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id('btnSubmit').click()


def search_fun(driver, url, username, password):
    open_url(driver, url)
    login_func(driver, username, password)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    id_frame = id_li + '-frame'
    driver.switch_to.frame(id_frame)
    driver.find_element_by_id('searchNumber').send_keys('841')
    driver.find_element_by_id('searchBtn').click()
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-2']//td[@field='number']/div").text
    return num
