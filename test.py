### THIS FILE EXISTS SO I CAN TEST THINGS -> Welcome at Nuclear Test Site NO. 1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print("test.py - Wellcome in test script!")
    driver = webdriver.Firefox()
    driver.get("https://db.bepis.moe/koikatsu")
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Ayaka")
    tag_input = driver.find_element(By.ID, "tag")
    tag_input.send_keys("Genshin_Impact")
    tag_input.submit()

    i2 = 1

    #This works
    download_selector = "document.querySelector('#inner-card-body > div:nth-child("+str(i2)+") > div > div > a.btn.btn-primary.btn-sm').click();";#selenium don't like that XD
    time.sleep(3)
    driver.execute_script(download_selector)

    #This works TOO
    download_button = driver.find_element(By.CSS_SELECTOR, "#inner-card-body > div:nth-child("+str(i2)+") > div > div > a.btn.btn-primary.btn-sm")  # <-- the selector problem?
    download_button.click()


if __name__ == "__main__":
    main()



