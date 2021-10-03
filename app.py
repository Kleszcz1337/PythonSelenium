from selenium import webdriver
from time import sleep

PATH = r"your path to chrome driver"
driver = webdriver.Chrome(PATH)

EMAIL_ADDRESS = "email"
PASSWORD = "password"

driver.get("https://addmefast.com/free_points/tiktok_followers")

Login = driver.find_element_by_xpath('//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[1]')
Login.send_keys(EMAIL_ADDRESS)
Password = driver.find_element_by_xpath('//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[2]')
Password.send_keys(PASSWORD)

buttonlogin = driver.find_element_by_xpath('//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[3]').click()

sleep(3)
TiktokSection = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[20]/a').click()
sleep(7)
TiktokLike = driver.find_element_by_class_name('btn3').click()


sleep(5)
print(driver.title)


