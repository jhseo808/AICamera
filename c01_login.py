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

# PTZ_PTZ 제어
zoom_in = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[1]/div[1]/button')
zoom_out = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[1]/div[3]/button')
focus_in = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[3]/div[1]/button')
focus_out = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[3]/div[3]/button')
focus_auto = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[5]/div/button')

# PTZ 제어
btn_menu.click()
ptz_control = [zoom_in, zoom_out, focus_in, focus_out, focus_auto]
for ptz in ptz_control:
    action.click_and_hold(ptz).pause(1).release(ptz).perform()
    print(ptz, 'ok')

slider_zoom = driver.find_element(By.XPATH, '//*[@id="ptz_panel"]/div/div[1]/div[7]/div/span/span[1]/span[6]')
action.click_and_hold(slider_zoom).move_by_offset(50, 0).move_by_offset(-50, 0).release().perform()
print('Direct Zoom ok')

# PLAYER CONTROL_라이브 제어
live_control = driver.find_element(By.ID, 'player_control_pannel')
live_control.click()
time.sleep(2)

# display mode
screen_real = driver.find_element(By.XPATH, '//*[@id="display_list"]/div[1]/label/div')
screen_full = driver.find_element(By.XPATH, '//*[@id="display_list"]/div[2]/label/div')
screen_custom = driver.find_element(By.XPATH, '//*[@id="display_list"]/div[3]/label/div')

# screen_full.click()
# print('screen_full ok')
# time.sleep(2)
# action.send_keys(Keys.ESCAPE).perform()
screen_custom.click()
slider_screen = driver.find_element(By.XPATH, '//*[@id="colMenu1"]/div/div[2]/li/span/span[1]/span[6]')
action.click_and_hold(slider_screen).move_by_offset(50, 0).move_by_offset(-50, 0).release().perform()
print('screen_custom ok')
screen_real.click()
print('screen_real ok')
time.sleep(2)

# protocol
