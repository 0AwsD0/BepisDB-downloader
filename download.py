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
    print("WARNING: Some card weigh a lot even over 25MB - if your intewrnet is slow CHANGE WAIT TIME between card downloads to even 10 seconds!")

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

        #just set the loop to be true until the "Next" button is "disabled" than flip the flag to exit loop // if Next button DISABLED flag = 0
        #LOOP HERE
        flag = 1
        while(flag == 1):
            i = 2
            print(f"Page {i-1}")
            print("Sleep for 5 seconds to let the website load...")
            time.sleep(5)
            #SECOND LOOP HERE 24 cards on one page so from 1 <= 24
            i2 = 1
            while(i2<=24):
                download_button = driver.find_element(By.CSS_SELECTOR, "#inner-card-body > div:nth-child(" + str(i2) + ") > div > div > a.btn.btn-primary.btn-sm")
                download_button.click()
                print(f"The download button clicked. Waiting 3 Seconds for card to be downloaded. Downloading card number: {i2}")
                time.sleep(3)
                i2 += 1
            flag = 0 #it's here to test the lines above move down later



        # Next Button "a[href=/koikatsu?page="+i+"]" #for first loop i = 2 coz "?page=2"
        #below localize and click next button if active if not set flag to 0


        # button a class =  ->  page - link WHERE text is Next / Next button - if it's not "page-item disabled" than click and loop again if it's disabled than stoop loop



        # driver.quit()

    except Exception:
        print("Exception in basic_download(): "+Exception)



def main():
    print("download.py")

if __name__ == "__main__":
    main()