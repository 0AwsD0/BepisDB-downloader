import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def download(**data):
    print("Download function invoked with arguments: ", data)


#below code checks if the basic option is selected - if yes -> the universal function will be invoked | if no -> the advanced functions will be invoked - tailored to the data that is for set game type
    try:
        if data["mode"] == "basic":
            print("Basic mode activated.")
            if data["game"] == "KK":
                url = "https://db.bepis.moe/koikatsu"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "AA2":
                url = "https://db.bepis.moe/aa2"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "HS":
                url = "https://db.bepis.moe/honeyselect"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "PH":
                url = "https://db.bepis.moe/playhome"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "AI_HS2":
                url = "https://db.bepis.moe/aishoujo"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "COM3D2":
                url = "https://db.bepis.moe/com3d2"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "SH":
                url = "https://db.bepis.moe/summerheat"
                basic_download(url, data["name"], data["tags"])
            elif data["game"] == "HC":
                url = "https://db.bepis.moe/honeycome"
                basic_download(url, data["name"], data["tags"])
            else:
                print("ERROR! Unknown value at key -> 'game' | Program will exit in 5 seconds.")
                time.sleep(5)
                exit(code=1)
    except Exception:
        print("Advanced mode activated.")
        #OR checking one by one if certain variables are present in dictionary and if they are running line in selenium that will fill parts of the form
        #the above would avoid the repetition of code and below if statement but idk what's better / faster while running - probably gonna try both and check if it makes any difference
        if data["game"] == "KK":
            url = "https://db.bepis.moe/koikatsu"
            #KK()
        elif data["game"] == "AA2":
            url = "https://db.bepis.moe/aa2"
            #AA2()
        elif data["game"] == "HS":
            url = "https://db.bepis.moe/honeyselect"
            #HS()
        elif data["game"] == "PH":
            url = "https://db.bepis.moe/playhome"
            #PH()
        elif data["game"] == "AI_HS2":
            url = "https://db.bepis.moe/aishoujo"
            #AI_HS2()
        elif data["game"] == "COM3D2":
            url = "https://db.bepis.moe/com3d2"
            #COM3D2()
        elif data["game"] == "SH":
            url = "https://db.bepis.moe/summerheat"
            #SH()
        elif data["game"] == "HC":
            url = "https://db.bepis.moe/honeycome"
            #HC()
        else:
            print("ERROR! Unknown value at key -> 'game' | Program will exit in 5 seconds.")
            time.sleep(5)
            exit(code=1)

def basic_download(url, name, tags):
    print("Basic download function invoked.")
    #I need to let user config wait time and provide some values or idk explain it in documentation and readme.md
    #OR
    #I may try using watchdog or directory scan to check if file exists -> the card and waiting until it does so there is no need for download interval - it downloads only if previous card is downloaded
    print("WARNING: Some cards weigh a lot, even over 25MB - if your intewrnet is slow CHANGE WAIT TIME between card downloads to even 10 seconds!")

    try:
        url = url
        name = name
        tags = tags
        print("url: ", url, " name: ", name," tag: ", tags)
        #selenium code below
        options = webdriver.FirefoxOptions()
        #options.add_argument("-headless")
        #driver = webdriver.Firefox(options=options)
        driver = webdriver.Firefox()
        driver.get(url)

        # I know I can just make up the link to the website since it's uses GET method like "https://db.bepis.moe/koikatsu?name=aaaa&tag=bbbb" but I want to try use the way below
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys(name)
        tag_input = driver.find_element(By.ID, "tag")
        tag_input.send_keys(tags)
        tag_input.submit()

        print("Waiting 5 seconds for page to load...")
        time.sleep(5)

        #just set the loop to be true until the "Next" button is "disabled" than flip the flag to exit loop // if Next button DISABLED flag = 0
        i = 2
        i2 = 1
        flag = 1

        #base url - the url2 is for adding '&page='+i and than reseting it back to normal before adding next &page
        url = driver.current_url

        while (flag == 1):
            try:
                while (i2 <= 24):
                    print(f"Downloading card number: {i2}")
                    download_selector = "document.querySelector('#inner-card-body > div:nth-child(" + str(i2) + ") > div > div > a.btn.btn-primary.btn-sm').click();";
                    time.sleep(3)
                    driver.execute_script(download_selector)
                    i2 += 1
                #JS to check the Next button if it's parent dont have "disabled" attrib, than click it and continue, if it does - download finished -> Raise flag - exit loop. exit(0)
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
                print("Getting url...")
                url2 = url
                print("Got url - adding page number...")
                url2 += "&page=" + str(i)
                print("I got url - waiting 5 seconds for page to load...")
                driver.get(url2)
                time.sleep(5)
                i2 = 1
                i += 1
                #Below IF for testing only - remove later
                if(i >= 5):
                    flag == 0
            except Exception:
                print("The download failed! Exiting in 5 seconds.")
                time.sleep(5)
                exit(1)

        # driver.quit()

    except Exception:
        print("Exception in basic_download(): "+Exception)



def main():
    print("download.py")

if __name__ == "__main__":
    main()