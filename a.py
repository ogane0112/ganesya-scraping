from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# EdgeDriverのパスを指定
service = Service(executable_path=r"msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Excelファイルを読み込む
df = pd.read_excel("input.xlsx")

# IMEI列からデータを取得し、結果を格納するリストを作成
results = []

try:
    for imei in df['IMEI']:
        driver.get(r'https://network.mobile.rakuten.co.jp/restriction/')

        # ページが完全にロードされるまで待機
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # IMEIを入力
        element = driver.find_element(By.NAME, 'imei')
        element.send_keys(str(imei))
        time.sleep(2)
        button = driver.find_element(By.ID, 'search')
        
        # ボタンをクリックする
        button.click()
        
        # 結果が表示されるまで待機
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search-result'))
        )
        result = driver.find_element(By.ID, "search-result")
        
        # 結果をリストに追加
        results.append(result.text)
        time.sleep(2)  # 次の検索をする前に少し待機

finally:
    driver.quit()

# 結果をDataFrameに追加
df['Result'] = results

# 結果をExcelに保存
df.to_excel("output.xlsx", index=False)
