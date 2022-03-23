import requests as req
import numpy as np
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import selenium

config = {             
		"timeout" : 10, #in seconds
		
        "domain" : "https://www.instagram.com/",
        "username" : "xxx",
        "password" : "xxx",

        "image_path" : "xxx/xxx/xxx",
        "caption" : "xxxxxxxxxxxxxxxxxxxx"
    }

delay_Time = 3

def connectToPage(driver,k):
    count = 0
    while True:
        try:
            req.get(k["domain"])
            driver.get(k["domain"])
            break
        except req.exceptions.ConnectionError:
            print(f"website down, keep trying since {count} s")
            if count == k["timeout"]:
                print("Timed Out")
                break
            time.sleep(1)

def logIn(driver,k):
    connectToPage(driver,k)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input').send_keys(k["username"])
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input').send_keys(k["password"])
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[1]/form/div/div[3]/button/div').click()

def uploadPic(driver,k):
    connectToPage(driver,k)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    time.sleep(delay_Time)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div/svg').click()
    time.sleep(delay_Time)
    driver.find_element_by_id('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys(k["image_path"])
    time.sleep(delay_Time)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    time.sleep(delay_Time)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    time.sleep(delay_Time)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea').send_keys(k["caption"])
    time.sleep(delay_Time)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    time.sleep(delay_Time)

def main(driver):
	start_time = time.time()
	while True:
		actual_time = time.time()
		if time.asctime(time.localtime(actual_time)) == config["time"]:
			logIn(driver, config)
			time.sleep(delay_Time)
			uploadPic(driver, config)
			break
		elif actual_time-start_time > config["timeout"]*60:
			print("Error: Time Out")
			break

def test(driver):
    count = 0
    while True:
        try:
            req.get(config["domain"])
            driver.get(config["domain"])
            logIn(driver, config)
            time.sleep(delay_Time)
            uploadPic(driver, config)
            break
        except req.exceptions.ConnectionError:
            print(f"website down, keep trying since {count} s")
            if count == config["timeout"]:
                print("Timed Out")
                break
            time.sleep(1)

if __name__ == '__main__':
	driver = webdriver.Chrome('./chromedriver')
	test(driver)
