import time
#--coding:gb18030--
from  appium import webdriver


desired_caps={
    "platformName":"Android",
    "deviceName":"eaaed474",
    "platformVersion":"10",
    "appPackage":"com.tencent.mm",
    "appActivity":"com.tencent.mm.ui.LauncherUI",
    "noReset":True,
    "chromeOptions":{"androidProcess":"com.tencent.mm:tools"} ,#启动公众微信号
    'automationName':'UiAutomator1',
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(10)
#查找搜索
driver.find_element_by_id("com.tencent.mm:id/f8y").click()
time.sleep(3)
driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys("诺亚荣耀")
time.sleep(4)
driver.find_element_by_xpath("//*[@text='诺亚荣耀保险经纪']").click()
#优选产品
driver.find_element_by_xpath("//*[@text='优选产品']").click()
#全部产品
driver.find_element_by_xpath("//*[@text='全部产品']").click()

#H5页面的滑动
target=driver.find_element_by_xpath("//*[@id='productList']/div[5]")
driver.execute_script("arguments[0].scrollIntoView();", target)


#









