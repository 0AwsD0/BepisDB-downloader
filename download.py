import time
from time import sleep

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

def basic_download(url, name, tag):
    print("Basic download function invoked.")
    url = url
    name = name
    tag = tag
    print("url: ", url, " name: ", name," tag: ", tag)
    #selenium code below

def main():
    print("download.py")

if __name__ == "__main__":
    main()