from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time 


def send_email(email_list):
    
    with open(email_list, 'r', encoding='utf-8') as file:
        emails = [x.strip() for x in file.readlines()]


    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', 'False')

    service = Service(executable_path=ChromeDriverManager().install())    
    driver = webdriver.Chrome(service=service, options=options)

    email_len = len(emails)
    count = 1
    try:
        driver.maximize_window()
        driver.get('https://web4.beget.email/')
        time.sleep(3)
        login = 'seofast@selfideveloping.ru'
        password = 'fi5kL*Er'
       
         
        
        login_input = driver.find_element(By.XPATH, '//input[@id="rcmloginuser"]')   
        login_input.send_keys(login) 
        time.sleep(1)
        password_input = driver.find_element(By.XPATH, '//input[@id="rcmloginpwd"]')
        password_input.send_keys(password)
        time.sleep(1)
        send_button = driver.find_element(By.XPATH, '//button[@id="rcmloginsubmit"]')
        send_button.click()
        time.sleep(10)

        for email in emails[:100]:
            time.sleep(2)
            # Написать сообщение
            action_buttons = driver.find_element(By.XPATH, '//span[@class="action-buttons"]/a')
            ActionChains(driver).move_to_element(action_buttons).click(action_buttons).perform()
            time.sleep(10)
            
            try:
                # Кому
                email_input = driver.find_element(By.XPATH, '//*[@id="compose_to"]/div/div/ul/li/input')
            except NoSuchElementException:
                time.sleep(10)
                email_input = driver.find_element(By.XPATH, '//*[@id="compose_to"]/div/div/ul/li/input')
            
            email_input.send_keys(email)
            time.sleep(1)        
           
            # Тема
            team_input = driver.find_element(By.XPATH, '//input[@id="compose-subject"]')
            time.sleep(1)
            team_input.send_keys('Продвижение интернет магазина')
            time.sleep(1)
            
            # Текст письма
            textaera = driver.find_element(By.XPATH, '//textarea[@id="composebody"]')
            textaera_text = 'Добры день. У вас интересны интернет магазина, но я трудом нашла Ваш ресурс в поисковом выдаче. Предлагаю хороший сервис для вывода вашего сайта в ТОП-3 по основному запросу. Подробнее по ссылке  - http://proflinks.ru/registration/30744  Спасибо)'
            textaera.send_keys(textaera_text)
            time.sleep(2)

            # Отправить 
            send_button = driver.find_element(By.XPATH, '//button[@id="rcmbtn110"]')
            ActionChains(driver).move_to_element(send_button).click(send_button).perform()
            time.sleep(10)

            print(f'[Send Email] {count} / {email_len}')
            count += 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()        

def main():
    send_email(email_list='email_list.txt')


if __name__ == '__main__':
    main()