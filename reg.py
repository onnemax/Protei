import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://192.168.56.102/cgi-bin/badstore.cgi?action=loginregister")


name = driver.find_element(By.NAME, "fullname")#Поиск элемента
name.send_keys("Максим Мартынюк")#Заполнение


email = driver.find_element(By.XPATH, value="//font/form[2]/p[1]/input")
email.send_keys("onnemax@mail.ru")


passwd = driver.find_element(By.XPATH, value="//font/form[2]/p[2]/input")
passwd.send_keys("12345") 


color = driver.find_element(By.NAME,"pwdhint")
color.send_keys("orange")

reg = driver.find_element(By.NAME, "Register")
reg.click() #Нажатие на кнопку


iframe = driver.find_element(by=By.XPATH,
               value="/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[2]/td[1]/iframe")#Шапка

assert iframe.text != "{Unregistered User}"#Проверка отображения имени в шапке

driver.switch_to.default_content()
