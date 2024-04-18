import requests
from datetime import datetime, timedelta
import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://scr.cyc.org.tw/tp13.aspx?module=login_page&files=login")
    page.get_by_role("button", name="OK").click()
    page.locator("#ContentPlaceHolder1_loginid").click()
    page.locator("#ContentPlaceHolder1_loginid").fill("A196414864")
    page.locator("#loginpw").click()
    page.locator("#loginpw").fill("Jet..0215")
    page.locator("#login_but").click()
    #保存storage state 到指定的文件
    storage = context.storage_state(path="auth/state.json")

    cookies = context.cookies()

    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    page.goto("https://scr.cyc.org.tw/tp13.aspx")

    target_cookie_name = 'ASP.NET_SessionId'

    context.close()
    browser.close()

    for cookie in cookies:
        if cookie['name'] == target_cookie_name:
            print("找到目標 cookie！")
            print("目標 cookie 的值是:", cookie['value'])
            return cookie['value']
        else:
            print("找不到目標 cookie。")

    # ---------------------

def check_booking_status(session, QPid,QTime):
    current_date = datetime.now()
 
    # 往後推 13 天
    future_date = current_date + timedelta(days=13)
 
    # 格式化日期為 "年/月/日" 字串
    future_date_str = future_date.strftime("%Y/%m/%d")
 
    # 第一段程式碼
    url = "https://scr.cyc.org.tw/tp13.aspx"
    params = {
        "module": "net_booking",
        "files": "booking_place",
        "StepFlag": "25",
        "QPid": QPid, # 1174.1175.1176
        "QTime": QTime, # 19.20
        "PT": "1",
        "D": future_date_str
    }
    cookies = {
        "ASP.NET_SessionId": session
    }
    response = requests.get(url, params=params, cookies=cookies)
    print(response.text)
    return response.text
 
def check_payment_status(session):
    # 第二段程式碼
    url = "https://scr.cyc.org.tw/tp13.aspx"
    params = {
        "module": "member",
        "files": "orderx_mt"
    }
    cookies = {
        "ASP.NET_SessionId": session
    }
    response = requests.get(url, params=params, cookies=cookies)
    if "未繳費" in response.text:
        print("已搶票成功!")
        return True
    else:
        print("搶票中...")
        return False
 
# 重複執行直到顯示"OK"
with sync_playwright() as playwright:
    session = run(playwright)
    while True:
        for qpid in [1174, 1175, 1176]:
            for qtime in [19, 20]:
                check_booking_status(session, qpid, qtime)
        if check_payment_status(session):
            break
        time.sleep(2)
