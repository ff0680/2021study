# 获取坐标
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

caps = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "192.168.56.101:5555",
    "appPackage": "com.xueqiu.android",  # aapt dump badging apk
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": False
}

from appium.webdriver import Remote

driver = Remote(desired_capabilities=caps,
                command_executor='http://127.0.0.1:4723/wd/hub')  # 初始化Remote

e = driver.find_element_by_id('')
rect = e.rect  # 可以打印坐标的x,y,width,height
strat_x = rect['x']  # 元素的起始坐标
start_y = rect['y']  # 元素的起始坐标
width = rect['width']
height = rect['height']

# 第一个点
point1 = {'x': strat_x + width / 6, 'y': start_y + height / 6}
# 第二个点
point2 = {'x': strat_x + width / 6 * 3, 'y': start_y + height / 6}
# 第三个点
point3 = {'x': strat_x + width / 6 * 5, 'y': start_y + height / 6}
# 初始化TouchAction
touch = TouchAction(driver)
# press 点击   move_to 移动  release：释放
touch.press(**point1).wait(200).move_to(
    **point2).wait(200).move_to(
    **point3).release().perform()

# 多个手指进行操作MultiAction


















