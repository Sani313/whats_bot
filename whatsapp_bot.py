from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

users = input('enter the users:')
a = users.split(',')
names = list(a)

message =input('enter you message: ')

count = int(input('how many times:  '))

input('\n\nrun??\n\n')

for user in names:
    name = driver.find_element(By.XPATH,f'//span[@title="{user}"]')
    name.click()
    sleep(1)
    box = driver.find_element(By.XPATH,'//div[@class="_ak1l"]')
    for N in range(count):
        for char in message:
            box.send_keys(char)
            sleep(0.1)
        emojy = driver.find_element(By.XPATH,'//div[@class="x1n2onr6 x78zum5 xy5a6gi x15cnf4b x1v3ui1v x1i64zmx x1emribx x1pge628"]')
        emojy.click()
        sleep(0.5)
        driver.find_element(By.XPATH,'//span[@class="b82 emojik wa"]').click()
        sleep(0.5)
        driver.find_element(By.XPATH,'//span[@class="b82 emojik wa"]').click()
        sleep(0.5)
        driver.find_element(By.XPATH,'//div[@class="_ak1t _ak1u"]').click()

sleep(5)
driver.quit()


