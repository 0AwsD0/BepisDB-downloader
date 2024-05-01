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

        #list and click the download buttons (loop) with certain intervals since website don;t like bulk download ~make wait time so the bigger cards can be downloaded ~ 3 seconds
        #the value below must be 2 on the beginning -> after "Next" button is clicked -> i++
        i = 2
        #LOOP HERE
        print("Page "+(i-1))

        #SECOND LOOP HERE 24 cards so from 1 <= 24
        i2 = 1
        download_button = driver.find_element(By.CSS_SELECTOR,"inner-card-body > div:nth-child('"+i2+"') > div > div > a.btn.btn-primary.btn-sm")
        download_button.click()
        # inner-card-body > div:nth-child('+number+') > div > div > a.btn.btn-primary.btn-sm').click()

        # Next Button "a[href=/koikatsu?page="+i+"]" #for first loop i = 2 coz "?page=2"
        #below localize and click next button if active


        #here loop including that inside -> just set the loop to be true until the "Next" button is "disabled"
        # button a class =  ->  page - link WHERE text is Next / Next button - if it's not "page-item disabled" than click and loop again if it's disabled than stoop loop



        # driver.quit()

    except Exception:
        print("Exception in basic_download(): "+Exception)



def main():
    print("download.py")

if __name__ == "__main__":
    main()