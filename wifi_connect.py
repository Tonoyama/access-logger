from selenium import webdriver
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


SUTUDENT_ID = os.environ.get("SUTUDENT_ID")
SUTUDENT_PASSWORD = os.environ.get("SUTUDENT_PASSWORD")


options=webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://lanauth.it.osakac.ac.jp/")

time.sleep(5)

login_id = driver.find_element_by_name("username")
login_id.send_keys(SUTUDENT_ID)

# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys(SUTUDENT_PASSWORD)

#ログインボタンをクリック
login_btn = driver.find_element_by_name("Submit")
login_btn.click()

time.sleep(5)

driver.close()