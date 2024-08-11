import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#BTW selenium 420 ~blaze it XD

def download(**data):
    print("Download function invoked with arguments: ", data)

#below code checks if the basic option is selected - if yes -> the universal function will be invoked | if no -> the advanced functions will be invoked - tailored to the data that is for set game type
    if data["mode"] == "basic":
        basic_download(data["url"], data["name"], data["tags"], data["start_from"])
    else:
        advanced_download(**data)


def basic_download(url, name, tags, start_from):
    print("Basic download function invoked.")
    #I need to let user config wait time and provide some values or idk explain it in documentation and readme.md
    #OR
    #I may try using watchdog or directory scan to check if file exists -> the card and waiting until it does so there is no need for download interval - it downloads only if previous card is downloaded
    print("WARNING: Some cards weigh a lot, even over 25MB - if your internet is slow - CHANGE WAIT TIME - between card downloads to even 20 seconds!")
    print("The corresponding SLEEP functions in code have comments above, surrounded by #.")

    url = url
    name = name
    tags = tags
    print("url: ", url, " name: ", name," tag: ", tags," start_from: ", start_from)

    #selenium code below
    #options = webdriver.FirefoxOptions()
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
    # base url - the url2 is for adding '&page='+i and than reseting it back to normal before adding next &page
    url = driver.current_url

    #logic for start from page n
    if not start_from:
        print("Starting from page 1")
        #iterator for page 2 //see code near line ~121
        i = 2
    else:
        start_from = str(start_from)
        url_page_start = driver.current_url + "&page=" + start_from
        driver.get(url_page_start)
        print("Starting from page: " + start_from)
        print("Waiting 5 seconds for page to load...")
        #iteretor for next page from number provided by user
        i = int(start_from)
        i = i+1 #this addition is required coz function below adds page number after executing url
        time.sleep(5)


    #just set the loop to be true until the "Next" button is "disabled" than flip the flag to exit loop // if Next button DISABLED flag = 0

    i2 = 1
    flag = 1

    while (flag == 1):
        try:
            try:
                while (i2 <= 24):
                    print(f"Downloading card number: {i2}")
                    download_selector = "document.querySelector('#inner-card-body > div:nth-child(" + str(i2) + ") > div > div > a.btn.btn-primary.btn-sm').click();"
                    driver.execute_script(download_selector)
                    ######################################
                    #BELOW TIME FOR CARD TO BE DOWNLOADED#
                    ######################################
                    time.sleep(5)
                    i2 += 1
            except Exception:
                print("The download FINISHED!")
                print("There were less than 24 cards on last page.")
                print(">>OR There is slight chance, that website got down.")
                #    flag == 0 + go back to main() // or leave like that to exit program
                print("You can close the spawned browser now.")
                print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
                print("-------------------")
                print("Exiting in 10 seconds.")
                time.sleep(10)
                #driver.quit()
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
            ########################################################################
            #sleep below for script and mainly for last card/cards to be downloaded#
            ########################################################################
            time.sleep(10)
            print("Button state = "+button_state)
            if(button_state == "Disabled"):
                print("Download FINISHED!")
                #    flag == 0 + go back to main() // or leave like that to exit program
                print("You can close the spawned browser now.")
                print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
                print("-------------------")
                print("Exiting in 5 seconds.")
                #driver.quit()
                time.sleep(5)
                exit(0)
            print("Getting url...")
            url2 = url
            url2 += "&page=" + str(i)
            print("Got url - adding page number...")
            print("Url: " + url2)
            print("Waiting 5 seconds for page to load...")
            driver.get(url2)
            time.sleep(5)
            i2 = 1
            i += 1
        except Exception:
            print("The download failed. //loop "+Exception)
            print("You can close the spawned browser now.")
            print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
            print("-------------------")
            print("Exiting in 5 seconds.")
            time.sleep(5)
            #driver.quit()
            exit(1)

#I tried to make below shorter since the download LOOP is same as in basic download, but the driver must be initialized in same method, so I can't do it without spawning additional unnecessary browsers
#But in other end it's easier to deal with code that is simpler, even if there is more of it. ~Terry would approve
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
    print("WARNING: Some cards weigh a lot, even over 25MB - if your internet is slow CHANGE WAIT TIME between card downloads to even 10 seconds!")
    print("The corresponding SLEEP functions in code have comments above, surrounded by #.")

    url = data["url"]
    name = data["name"]
    tags = data["tags"]

    show_hidden = data["show_hidden"]
    show_only_featured = data["show_only_featured"]
    order_by = data["order_by"]

    #selenium code below

    #options = webdriver.FirefoxOptions()
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
        #else:#for test
            #print("gender > empty")#for test
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
    try:
        start_from = data["start_from"]
    except:
        print("modded_content not found in datased - skipping")

    #submit whole form
    tag_input.submit()

    print("Waiting 5 seconds for page to load...")
    time.sleep(5)

    # base url - the url2 is for adding '&page='+i and than reseting it back to normal before adding next &page
    url = driver.current_url

    #logic for start from page n
    if not start_from:
        print("Starting from page 1")
        #iterator for page 2 //see code near line ~121
        i = 2
    else:
        start_from = str(start_from)
        url_page_start = driver.current_url + "&page=" + start_from
        driver.get(url_page_start)
        print("Starting from page: " + start_from)
        print("Waiting 5 seconds for page to load...")
        #iteretor for next page from number provided by user
        i = int(start_from)
        i = i+1 #this addition is required coz function below adds page number after executing url
        time.sleep(5)

    #just set the loop to be true until the "Next" button is "disabled" than flip the flag to exit loop // if Next button DISABLED flag = 0
    i2 = 1
    flag = 11

    #base url - the url2 is for adding '&page='+i and than reseting it back to normal before adding next &page
    url = driver.current_url

    while (flag == 1):
        try:
            try:
                while (i2 <= 24):
                    print(f"Downloading card number: {i2}")
                    download_selector = "document.querySelector('#inner-card-body > div:nth-child(" + str(i2) + ") > div > div > a.btn.btn-primary.btn-sm').click();"
                    driver.execute_script(download_selector)
                    ######################################
                    #BELOW TIME FOR CARD TO BE DOWNLOADED#
                    ######################################
                    time.sleep(5)
                    i2 += 1
            except Exception:
                print("The download FINISHED!")
                print("There were less than 24 cards on last page.")
                print(">>OR There is slight chance, that website got down.")
                #    flag == 0 + go back to main() // or leave like that to exit program
                print("You can close the spawned browser now.")
                print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
                print("Exiting in 10 seconds.")
                time.sleep(10)
                #driver.quit() - uncomment to auto close NOT browser - commented to let user check if card download finished -> some of them take their time by some reason
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
            ########################################################################
            #sleep below for script and mainly for last card/cards to be downloaded#
            ########################################################################
            time.sleep(10)
            print("Button state = "+button_state)
            if(button_state == "Disabled"):
                print("Download FINISHED!")
                #    flag == 0 + go back to main() // or leave like that to exit program
                print("You can close the spawned browser now.")
                print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
                print("-------------------")
                print("Exiting in 5 seconds.")
                #driver.quit()
                time.sleep(5)
                exit(0)
            print("Getting url...")
            url2 = url
            print("Got url - adding page number...")
            url2 += "&page=" + str(i)
            print("Url: "+url2)
            print("Waiting 5 seconds for page to load...")
            driver.get(url2)
            time.sleep(5)
            i2 = 1
            i += 1
        except Exception:
            print("The download failed. ", Exception)
            print("You can close the spawned browser now.")
            print("But before you close it -> CHECK IF DOWNLOAD FINISHED.")
            print("-------------------")
            print("Exiting in 5 seconds.")
            time.sleep(5)
            #driver.quit()
            exit(1)

def main():
    print("download.py")

if __name__ == "__main__":
    main()