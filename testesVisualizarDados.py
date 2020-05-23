from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("E:\\chrome\\chromedriver.exe")
driver.implicitly_wait(100)

driver.get("https://5ec34f678a75200006f5ff4a--boring-poitras-1de61c.netlify.app")
driver.find_element_by_id("basic_username").click()
driver.find_element_by_id("basic_username").send_keys("admin@email.com")
driver.find_element_by_id("basic_password").send_keys("Admin@123")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("//div[@id='root']/section/aside/div/ul/li[3]/div").click()
driver.find_element_by_link_text("Perfil").click()

driver.maximize_window()
print("Implicit Wait Example")

inputElement = driver.find_element_by_id("lst-ib")
inputElement.send_keys("Techbeamers")
inputElement.submit()

driver.close()