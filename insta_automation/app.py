from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"


def login(chomedriver_path, username, password):
    """
    instagramへログインするための関数
    """
    driver = webdriver.Chrome(executable_path=chomedriver_path)
    driver.get(INSTAGRAM_URL)
    time.sleep(3)

    # ユーザー名とパスワードを入力
    driver.find_element_by_name("username").send_keys(Keys.ENTER, username)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.ENTER, password)
    time.sleep(1)

    # ログインボタンをクリック
    driver.find_element_by_class_name("L3NKy").click()
    time.sleep(1)
