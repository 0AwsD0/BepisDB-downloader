import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def advanced_download(**data):
    print("Advanced download function invoked.")
    print("DATA: ", data)
    '''
    ALL POSIBLE DATA:
    game
    name
    tags
    preset_type
    gender
    personality
    game_type
    modded_content
    order_by
    show_hidden
    show_only_featured
    '''
    #I need to let user config wait time and provide some values or idk explain it in documentation and readme.md
    #OR
    #I may try using watchdog or directory scan to check if file exists -> the card and waiting until it does so there is no need for download interval - it downloads only if previous card is downloaded
    print("WARNING: Some cards weigh a lot, even over 25MB - if your intewrnet is slow CHANGE WAIT TIME between card downloads to even 10 seconds!")
    ''' 
    try:
    '''
    url = data["url"]
    name = data["name"]
    tags = data["tags"]

    show_hidden = data["show_hidden"]
    show_only_featured = data["show_only_featured"]
    order_by = data["order_by"]

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

    #below mess to detect if "varible" (key) exists, if yes -> create the varible -> than use it to fill the form field
    try:
        preset_type = data["preset_type"]
        preset_type_input = Select(driver.find_element(By.ID, "type"))
        if (preset_type != ""):
            preset_type_input.select_by_value(preset_type)
    except:
        print("preset_type not found in datased - skipping")

    try:
        gender = data["gender"]
        gender_input = Select(driver.find_element(By.ID, "gender"))
        if (gender != ""):
            gender_input.select_by_value(gender)
        else:#for test
            print("gender > empty")#for test
    except:
        print("gender not found in datased - skipping")

    try:
        personality = data["personality"]
        personality_input = Select(driver.find_element(By.ID, "personality"))
        if (personality != ""):
            personality_input.select_by_value(personality)
    except:
        print("personality not found in datased - skipping")

    try:
        game_type = data["game_type"]
        game_type_input = Select(driver.find_element(By.ID, "type"))
        if (game_type != ""):
            game_type_input.select_by_value(game_type)
    except:
        print("game_type not found in datased - skipping")

    try:
        modded_content = data["modded_content"]
    except:
        print("modded_content not found in datased - skipping")

    #submit whole form
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
            print("Waiting 5 seconds for page to load...")
            driver.get(url2)
            time.sleep(5)
            i2 = 1
            i += 1
        except Exception:
            print("The download failed. ", Exception)
            print("Exiting in 5 seconds.")
            time.sleep(5)
            driver.quit()
            exit(1)
    ''' 
    except Exception:
        print("Exception in advanced_download(): ", Exception)
        print("Exiting in 5 seconds.")
        time.sleep(5)
        driver.quit()
        exit(1)

'''
def main():
    print("test2.py")

    mode = "advanced"
    game = "KK"
    url = "https://db.bepis.moe/koikatsu"
    name = "Ayaka"
    tags = "Genshin_Impact"
    gender = ""
    personality = "1"
    order_by = "" #<---- "" or 0
    show_hidden = "1"
    show_only_featured = ""
    advanced_download(mode= mode, game=game, url=url, name=name, tags=tags, gender=gender, personality=personality, order_by=order_by, show_hidden=show_hidden, show_only_featured=show_only_featured)

    #The Below Works TOO
'''
    mode = "advanced"
    game = "COM3D2"
    url = "https://db.bepis.moe/com3d2"
    name = ""
    tags = ""
    preset_type = "body"
    order_by = ""  # <---- "" or 0
    show_hidden = "1"
    show_only_featured = ""
    advanced_download(mode= mode, game=game, url=url, name=name, tags=tags,preset_type = preset_type, order_by=order_by, show_hidden=show_hidden, show_only_featured=show_only_featured)
    '''
if __name__ == "__main__":
    main()

#KEKW - that tests (.py)
#Do you read a code comments? If yes, then good for you!
#Should't I assert it?... get it? assert? XDDD