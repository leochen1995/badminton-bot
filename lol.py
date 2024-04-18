import requests
from datetime import datetime, timedelta
import time

def check_booking_status(QPid,QTime):
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
        "ASP.NET_SessionId": "f25jw0wsk3viglt0j54gdokz"
    }
    response = requests.get(url, params=params, cookies=cookies)
    print(response.text)
    return response.text

def check_payment_status():
    # 第二段程式碼
    url = "https://scr.cyc.org.tw/tp13.aspx"
    params = {
        "module": "member",
        "files": "orderx_mt"
    }
    cookies = {
        "ASP.NET_SessionId": "f25jw0wsk3viglt0j54gdokz"
    }
    response = requests.get(url, params=params, cookies=cookies)
    if "未繳費" in response.text:
        print("已搶票成功!")
        return True
    else:
        print("搶票中...")
        return False

# 重複執行直到顯示"OK"
while True:
    for qpid in [1174, 1175, 1176]:
        for qtime in [19, 20]:
            check_booking_status(qpid, qtime)
    if check_payment_status():
        break
    time.sleep(2)
