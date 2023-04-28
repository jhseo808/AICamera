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

# 메인 메뉴 리스트
btn_menu = driver.find_element(By.ID, 'menu_button')
btn_live = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[1]')
btn_playback = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[2]')
btn_setup = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[3]')
btn_logout = driver.find_element(By.XPATH, '//*[@id="sidebar-shortcuts-large"]/a[4]')

# setup
btn_menu.click()
btn_setup.click()
print('setup page ok')

# 설정 메뉴 리스트
set_info = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[1]/a')
set_video = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/a')
set_audio = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[3]/a')
set_rec = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[4]/a')
set_event = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[5]/a')
set_system = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[6]/a')

# 설정 > 비디오 & 이미지
set_video.click()

# 비디오 & 이미지 리스트
video_source = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[1]/a')
video_stream = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[2]/a')
video_smt_stream = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[3]/a')
video_image = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[4]/a')
video_pmask = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[5]/a')
video_dig_zoom = driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[6]/a')

# 설정 > 비디오 & 이미지 > 비디오 입력
video_source.click()

video_input1 = driver.find_element(By.ID, 'real_video_mode')
video_input2 = driver.find_element(By.ID, 'real_video_src')
video_input1.click()
print(video_input1.get_attribute("value"),'ok')
video_input2.click()
print(video_input2.get_attribute("value"),'ok')
