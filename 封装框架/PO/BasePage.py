# 封装工具层
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By


class Base:
    caps = {
        "platformName": "Android",
        "platformVersion": "6.0",
        "deviceName": "192.168.56.101:5555",
        "appPackage": "com.xueqiu.android",  # aapt dump badging apk
        "appActivity": "com.xueqiu.android.view.WelcomeActivityAlias",
        "noReset": False
    }

    def __init__(self,duration):
        self.driver = Remote(desired_capabilities=self.caps,
                             command_executor='http://127.0.0.1:4723/wd/hub')  # 初始化caps
        self.duration=1000 # 滑动持续时间，单位毫秒，默认None（一般设置500-1000毫秒比较合适）

    def Screenshots(self, save_file_name):
        """
        截图（待完善）
        :param save_file_name: 保存的地址
        :return:
        """
        self.driver.get_screenshot_as_file(save_file_name)

    def find_element(self, locator):
        """
        单个元素定位
        :param locator: 定位器
        :return: 定位到的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(locator))
            return ele
        except Exception as e:
            self.Screenshots("/Users/xiaoff/python/2020_study/appium/封装框架/screen_shot/定位问题.png")
            return '未定到到该元素', e

    def find_elements(self, locator):
        """
        元素定位有多个值
        :param locator: 定位器
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout=20).until(EC.presence_of_all_elements_located(locator))
            return ele
        except Exception as e:
            self.Screenshots("/Users/xiaoff/python/2020_study/appium/封装框架/screen_shot/定位问题.png")
            return '未定到到该元素', e

    """----滑动-----"""
    def get_width(self):
        """
        获取屏幕的宽度
        :return:
        """
        width=self.driver.get_window_size()['width']
        return width

    def get_height(self):
        """
        获取屏幕的高度
        :return:
        """
        height=self.driver.get_window_size()['height']
        return  height

    def swipe_to_right(self):
        """

        :return:
        """





















