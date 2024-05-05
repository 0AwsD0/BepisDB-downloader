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
    tag_input.send_keys("")
    tag_input.submit()

    time.sleep(5)

    #JS to check the Next button if it's parent dont have "disabled" attrib, than clikc if it does - download finished -> Raise flag - exit loop.
    #it's arguably better solution than seeaking for nth-childs (depends on number of pages with cards) in the page navigation

    i = 2
    flag = 1
    url = driver.current_url

    while (flag == 1):
        try:
            while (i2 <= 24):
                print(f"Downloading card number: {i2}")
                download_selector = "document.querySelector('#inner-card-body > div:nth-child(" + str(
                    i2) + ") > div > div > a.btn.btn-primary.btn-sm').click();";  # selenium don't like that XD
                time.sleep(3)
                driver.execute_script(download_selector)
                i2 += 1
            # JS to check the Next button if it's parent dont have "disabled" attrib, than click it and continue, if it does - download finished -> Raise flag - exit loop. exit(0)
            '''
            JS CODE BELOW - now make it into selenium XD
            02:40:20.388 xpath = "//a[contains(text(),'Next')]";
            02:40:20.405 "//a[contains(text(),'Next')]"
            02:40:34.097 var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            02:40:34.114 undefined
            02:42:05.285 matchingElement
            02:42:05.304
            <a class="page-link" href="/honeyselect?name=Ayaka">
            02:42:39.367 parentDiv = matchingElement.parentNode;
            02:42:39.389
            <li class="page-item disabled">
            02:42:43.478 parentDiv
            02:42:43.499
            <li class="page-item disabled">
            '''

            #if(parent div to (a - text=Next) have atrib 'Disabled'):
            #    print("Download finished! Exiting program in 5 seconds...")
            #    exit(0)

            print("Getting url...")
            url2 = url
            print("Got url - adding page number...")
            url2 += "&page=" + str(i)
            print("I got url - waiting 5 seconds for page to load...")
            driver.get(url2)
            time.sleep(5)
            i2 = 1
            i += 1
        except Exception:
            print("The download failed! Exiting in 5 seconds.")
            time.sleep(5)
            exit(1)


#Code below works
    ''' 
   
    i = 2
    i2 = 1

    #I may try using watchdog or directory scan to check if file exists -> the card and waiting until it does so there is no need for download interval - it downloads only if previous card is downloaded
    

    
    #The code below don't check the next button but instead directly edits url
    time.sleep(3)
    #IT JUST WORKS - need to add functionality that checks the number of pages it will add 16x details // well the first thought was propably better, so I
    while(i < 10):
        try:
            while(i2<=24):
                print(f"Downloading card number: {i2}")
                download_selector = "document.querySelector('#inner-card-body > div:nth-child("+str(i2)+") > div > div > a.btn.btn-primary.btn-sm').click();";  # selenium don't like that XD
                time.sleep(3)
                driver.execute_script(download_selector)
                i2 += 1
            print("Getting url...")
            url = driver.current_url
            print("Got url - adding page number...")
            #if statment checking if the '&page=' is present and adding if if int's not or cutting the number and adding new one
            url += "&page=" + str(i)
            print("I got url - waiting 5 seconds for page to load...")
            driver.get(url)
            time.sleep(5)
            i2 = 1
            i += 1
        except Exception:
            print("The download failed! Exiting in 5 seconds.")
            time.sleep(5)
            exit(1)
            
    '''

    # the detection for the number of pages in JS - checking the number inside DIV + Try Catch (Except) for downloading images, since website can have less than (max of) 24 cards
    ''' 
    i2 = 1


    #This works
    download_selector = "document.querySelector('#inner-card-body > div:nth-child("+str(i2)+") > div > div > a.btn.btn-primary.btn-sm').click();";#selenium don't like that XD
    time.sleep(3)
    driver.execute_script(download_selector)

    #This works TOO
    download_button = driver.find_element(By.CSS_SELECTOR, "#inner-card-body > div:nth-child("+str(i2)+") > div > div > a.btn.btn-primary.btn-sm")  #
    download_button.click()
 '''

if __name__ == "__main__":
    main()



