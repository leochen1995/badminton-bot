import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://scr.cyc.org.tw/tp13.aspx?Module=net_booking')
    page.get_by_role("img", name="羽球").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("cell", name="羽球場使用須知 場地公告 營業人名稱：中國青年救國團桃園市桃園國民運動中心 統一編號：72907876 場地預約須知 一、請先註冊會員資料，以「身分證字號」為登入帳號。 二、場地開放時間：依各中心官網公告為準，年節營業時間則另行公告。如遇颱風等天災，依照人事行政局宣布是否達停班停課為標準，另因舉辦活動、訓練期間及配合市政府活動等，得暫停開放預約。 三、可預約場地數：依中心官網公告為準，各中心視實際場地使用狀況開放可預約場地數量。 四、付款期限：運動中心會員預約成功後，請於10分鐘內完成刷卡付款，完成刷卡付款方為預約成功，操作逾時請重新預約。非運動中心會員請依原中心預約規定方式辦理。 五、非使用手機載具/愛心捐贈者，發票請至各中心櫃檯領取。 六、使用行為： 1.您使用本服務之一切行為必須符合當地或國際相關法令規範；對於使用者的一切行為，您須自行負擔全部責任。 2.您同意絕不為非法之目的或以非法方式使用本服務，與確實遵守中華民國相關法規及網際網路之國際慣例，並保證不得利用本服務從事侵害他人權益或違法之行為。 3.您於使用本站會員服務時應遵守以下限制： (1)有損他人人格或商標權、著作權等智慧財產權或其他權利內容。 (2)使用違反公共秩序或善良風俗或其他不法之文字。 (3)強烈政治、宗教色彩的偏激言論。 (4)未經本中心許可，不得利用本服務所提供其他資源，包括但不限於圖文資料庫、編寫製作網頁之軟體等，從事任何商業交易行為，或招攬廣告商或贊助人。 (5)不得使用不正方法或程式，侵入、攻擊、使用本系統，或其他類似之妨礙電腦使用之不正或違法行為。本中心經營單位判定會員有前述行為或其他違反會員服務條款時，得依情節按以下階段擇一對會員為期間內暫時停權或終止任一會員帳戶服務之權利(含本經營單位託管之所有中心)：(a)第一次違反時，停權14天；(b)第二次違反時，停權3個月；(c)第三次違反時，停權6個月；(d)第四次違反時，停權12個月。停權後之會員須於期滿後向本中心提出申請並經審核後，始得恢復會員帳戶服務之權利。 (6)未得本中心同意，利用本系統為營利行為或使其看似與本系統有關之營利行為。 (7)其他違反本站「會員服務條款」的內容。 (8)其他本中心判定不當之使用。 七、本中心專有權利：本服務所載，或本服務所連結之一切軟體或內容，或本中心之廣告商或合夥人所提供之內容，均受其著作權或其他專有權利或法律所保障。 八、線上預約完成後，若需異動場地日期、時間、場次，須先至【我的訂單】內進行「取消預約作業」後，持租用人證件至中心服務台辦理退費(20:15-20:30為系統自動關帳時間，暫時不受理退費)。 九、線上預約者，如欲取消場地，應於使用當日之「前2日之前」線上取消場地，並請於原場地使用當日之「7日內」至中心服務台辦理退費，若未取消而辦理退費或未於前2日前取消場地者，則記錄1次黑名單；原場地使用當日恕無法退費，達3次即停權180天。例如：預約5月20日場地者，請於5月17日(含)前線上取消場地，且須於5月26日(含)前至中心服務台辦理退費。 十、請自備球具(撞球場除外)或可於現場櫃台租借，球具租借辦法及費用依各中心收費規定。 十一、本中心場地未經允許，禁止私人教學。", exact=True).locator("img").click()
    page.get_by_role("button", name="OK").click()    
    page.locator("#ContentPlaceHolder1_loginid").click()
    page.locator("#ContentPlaceHolder1_loginid").fill("A196414864")
    page.locator("#ContentPlaceHolder1_loginid").press("Tab")
    page.locator("#loginpw").fill("Jet..0215")
    page.locator("#login_but").click()
    page.get_by_role("cell", name="01", exact=True).nth(2).click()
    page.get_by_text("晚上(18:00~22:00)").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("row", name="19:00~20:00 羽1 300", exact=True).get_by_role("img").click()
    browser = playwright.chromium.launch(headless=False)
    page.pause()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
