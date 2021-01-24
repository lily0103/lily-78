

import time
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