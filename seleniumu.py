from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# EdgeDriverのパスを指定
service = Service(executable_path=r"msedgedriver.exe")
driver = webdriver.Edge(service=service)
try:
    driver.get(r'https://network.mobile.rakuten.co.jp/restriction/')

    # ページが完全にロードされるまで待機
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # 必要な操作を実行
    # 例えばページタイトルを表示
    print(driver.title)
    element = driver.find_element(By.NAME, 'imei')
    element.send_keys("123456789012345")
    time.sleep(2)
    button = driver.find_element(By.ID, 'search')
    print("実行されました")
    # ボタンをクリックする
    button.click()
    result = driver.find_element(By.ID, "search-result")
    # ブラウザがすぐに閉じないように待機
    print(result.text) 
finally:
    driver.quit()

