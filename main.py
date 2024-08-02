from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from temp import *
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

def get_info_about_arbitr_by_f_i_o(**massage_number):
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 30)  # Увеличим время ожидания до 30 секунд
        
        driver.get('https://old.bankrot.fedresurs.ru/Default.aspx')
        
        # # Ожидание и клик по ссылке "Сообщения"
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_lnkMessages"]'))).click()
       
        # # Клик по элементу, который вызывает всплывающее окно
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphBody_mdsPublisher_tbSelectedText"]'))).click()
        # time.sleep(2)
        # iframe = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/script[2]')))  # Замените XPATH, если нужно
        # # driver.switch_to.frame(iframe)
        # # source = driver.page_source
        
        # # Сохранение HTML-кода в файл
        # with open("temp.html", 'w', encoding='utf-8') as file:
        #     file.write(source)
        
        # # Возвращение к основному контенту страницы, если нужно
        # driver.switch_to.default_content()
        all_cookies=driver.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        print(cookies_dict)


# куки из ефрсб
cookie = get_cookie()



# ссылка со всесеми сообщениями
# print(ol_massege_info(cookie=cookie))


# ссылка на арбитражного упровляющего
# number = 11465
# print(get_name_arbitr(cookie=cookie,number=number))

