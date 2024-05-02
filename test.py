### THIS FILE EXISTS SO I CAN TEST THINGS -> Welcome at Nuclear Test Site NO. 1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print("test.py - Wellcome in test script!")
    driver = webdriver.Firefox()
    driver.get("https://db.bepis.moe/koikatsu")
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("")
    tag_input = driver.find_element(By.ID, "tag")
    tag_input.send_keys("Uma_Musume")
    tag_input.submit()

    time.sleep(5)

    #JS to check the Next button if it's parent dont have "disabled" attrib, than clikc if it does - download finished -> Raise flag - exit loop.
    #it's arguably better solution than seeaking for nth-childs (depends on number of pages with cards) in the page navigation

    i = 2
    flag = 1
    url = driver.current_url

    next_button_script = """
    function next_button(){
    xpath = "//a[contains(text(),'Next')]";
    var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    parentDiv = matchingElement.parentNode;
    if(parentDiv.classList.contains('disabled') == true){
        var state = "Disabled";
        return 1;
    }
    else{
        var state = "Enabled";
        return 0;
    }
    }
    """
    print("Getting 'Next' button state...")
    driver.execute_script("""console.log("test");""")
    button_state = driver.execute_script(next_button_script) # It doesn't work. Why? | The script works when pasted into browser.
    time.sleep(2)
    driver.execute_script("""console.log("test2");""")
    print(button_state)
    driver.execute_script("""console.log("test3");""")

    """
        function next_button(){
        xpath = "//a[contains(text(),'Next')]";
        var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        parentDiv = matchingElement.parentNode;
        if(parentDiv.classList.contains('disabled') == true){
            var state = "Disabled";
            return 1;
        }
        else{
            var state = "Enabled";
            return 0;
        }
        }
        next_button();
        
        
        THIS DIDN'T WORK COZ THE FUNCTION LOOOOLLLL idk 
        
        """

if __name__ == "__main__":
    main()



