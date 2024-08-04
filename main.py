from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from temp import *
from decode import *
from data_raw import *
# функция которая дает cooki с сайта ефрсб
def get_cookie():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 30)  # Увеличим время ожидания до 30 секунд
        
        driver.get('https://old.bankrot.fedresurs.ru/Default.aspx')
        
        
        all_cookies=driver.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict



# куки из ефрсб
cookie = get_cookie()



# ссылка со всесеми сообщениями
# print(ol_massege_info(cookie=cookie))


# ссылка на арбитражного упровляющего
number = 3980 # номер арбитражного в реестре
name_and_number = ol_name_info(cookie=cookie,number=number)

data = made_raw_data_for_ol_massage(name=name_and_number[1],number=name_and_number[0],page_number='Page%243')
print(get_oll_mssege(cookie=cookie,data_raw=data))
