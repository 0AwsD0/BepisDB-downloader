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
        print("ERROR - basic_download couldn't be invoked. Is website down?")

    advanced_download()


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
                try:
                    while (i2 <= 24):
                        print(f"Downloading card number: {i2}")
                        download_selector = "document.querySelector('#inner-card-body > div:nth-child(" + str(i2) + ") > div > div > a.btn.btn-primary.btn-sm').click();"
                        time.sleep(4)
                        driver.execute_script(download_selector)
                        i2 += 1
                except Exception:
                    print("The download FINISHED!")
                    print("There were less than 24 cards on last page.")
                    print(">>OR There is slight chance, that website got down.")
                    #    flag == 0 + go back to main() // or leave like that to exit program
                    print("Exiting in 5 seconds.")
                    time.sleep(5)
                    driver.quit()
                    exit(0)
                next_button_script = """
                xpath = "//a[contains(text(),'Next')]";
                var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                parentDiv = matchingElement.parentNode;
                if(parentDiv.classList.contains('disabled') == true){
                    var state = "Disabled";
                    return state;
                }
                else{
                    var state = "Enabled";
                    return state;
                }
                """
                print("Getting 'Next' button state...")
                button_state = driver.execute_script(next_button_script)
                #sleep for script and mainly for last card/cards to download
                time.sleep(5)
                print("Button state = "+button_state)
                if(button_state == "Disabled"):
                    print("Download FINISHED!")
                    #    flag == 0 + go back to main() // or leave like that to exit program
                    print("-------------------")
                    print("Exiting in 5 seconds.")
                    driver.quit()
                    time.sleep(5)
                    exit(0)
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
                print("The download failed. "+Exception)
                print("Exiting in 5 seconds.")
                time.sleep(5)
                driver.quit()
                exit(1)
    except Exception:
        print("Exception in basic_download(): "+Exception)
        time.sleep(5)
        driver.quit()
        exit(1)

def advanced_download():
    print("Advanced download function invoked")
    #KK     download(game = game, name =  name, tags = tags, gender = gender, personality = personality, game_type = game_type, modded_content = modded_content, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #AA2   download(game = game, name =  name, tags = tags, gender = gender, personality = personality, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured) *
    #HS     download(game = game, name =  name, tags = tags, gender = gender, personality = personality, game_type = game_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #PH     download(game = game, name =  name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #AI_HS2 download(game = game, name =  name, tags = tags, gender = gender, personality = personality, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured) *
    #COM3D2 download(game = game, name =  name, tags = tags, preset_type = preset_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #SH     download(game = game, name =  name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #HC     download(game = game, name =  name, tags = tags, gender = gender, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)
    #AA2_&_AI_HS2

def main():
    print("download.py")

if __name__ == "__main__":
    main()