from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

#브라우저 꺼짐 방지
options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(3)
driver.maximize_window()

driver.get('http://172.16.6.207')
action = ActionChains(driver)

# 로그인
driver.find_element(By.ID, 'user').click()
(action.send_keys('admin').key_down(Keys.TAB).send_keys('admin1357').perform()) 
action.reset_actions
btn_login = driver.find_element(By.ID, 'login_submit')
btn_login.click()
print('Login ok')
driver.implicitly_wait(2)

# 메인 메뉴
btn_menu = driver.find_element(By.ID, 'menu_button')
btn_live = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[1]')
btn_playback = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[2]')
btn_setup = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[3]')
btn_logout = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[4]')
