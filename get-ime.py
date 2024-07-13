from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# EdgeDriverのパスを指定
service = Service(executable_path=r"msedgedriver.exe")
driver = webdriver.Edge(service=service)

try:
    driver.get('https://network.mobile.rakuten.co.jp/restriction/')

    # ページが完全にロードされるまで待機
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    element = driver.find_element(By.NAME, 'imei')
    element.send_keys("123456789012345")

    # 確認ボタンの要素を見つける（例えば、ボタンのIDが 'button_id' である場合）
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="確認"]'))
    )

    # ボタンをクリックする
    driver.execute_script("arguments[0].click();", confirm_button)

    # 必要に応じて、次のページやアクションがロードされるまで待機
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # ブラウザがすぐに閉じないように待機
    input("Press Enter to close the browser...")

finally:
    driver.quit()

