# BepisDB downloader - download character cards in bulk 
## Currently only console application
You are free to download the tool and use it for your private purposes. If you modify this program and you want to share it, make a fork. You have to include link to original repository on the top as shown here: Original repository: [link]

### If you need to download cards in bulk - or cards from certain tags etc. - This app is for you
I'm creating this application to learn some python and have it as a backup means of batch card download. I have my own browser add-on that I wrote in JS that works just fine, but I'm working on this solution in case my broken add-on cease to work. Also, I will not publish source code of that add-on because it's made just for me - so it's a little bit broken but to the extent I don't bother to fix it. And that's how this projects begins. The plan is to use Selenium and do even more functionality than the current browser add-on can do. Add-on worked by clicking download buttons in order, waiting hard-coded  amount of time until download is finished (to prevent multiple downloads, since the site didn;t like that), then clicking next button to move to the next page and repeated. Now I want to create another solution that allows user to create config files to automate download process even more. Will see where it will take me.
- I'm already seeing that writing JS Extension for that purpose was superfast, less complicated, but definitely both solutions have its pros and cons. (I probably will list them later on)

## How to use
- the software is in development, so it's advised to read code coments inside .py files to better understand it's inner workings
- the program is made for [db.bepis.moe](https://db.bepis.moe/) - so if you are uncertain what value you can enter into some fields -> go onto the website -> select game -? check what you can select and/or enter into search form
1. Select the game type
2. Select download type -> "basic"  allows to enter only "Name" and/or "Tag" to search -> "advanced" - allows to set up every search parameter available for selected game (work in progress on that one)
3. Enter value for each prompted field or click "Enter" to get default value.
4. Wait for download to finish.

## How it works
- The page for selected game is loaded and form is filled by the selenium. 
- After search button clicked, program waits 5 seconds for website to load. 
- It will download card every 5 seconds, to prevent multiple downloads, since the website doesn't like multiple downloads. (Some cards can be over 25MB that's why it's better to give it more than less time) //I may make function that check if the card download is finished than proceed to next card in the future.
- If the page had less than 24 cards on it, it's the last page (or only one) -> Download Finished
- If page have 24 cards but the "Next" button is disabled -> Download Finished
- If the button is active -> change url and load page -> start downloading cards, untill there is less than 24 cards on page or the "Next" button is disabled.

## Info for setup
- Some cards weigh a lot, even over 25MB - if your internet is slow - CHANGE WAIT TIME - between card downloads to even 20 seconds!
- The corresponding SLEEP functions in code have comments, surrounded by #. Just like shown below:
```
######################################
#BELOW TIME FOR CARD TO BE DOWNLOADED#
######################################
```
+The known issue is -> malwarebytes will kill the program if you run it from PyCharm, and possibly in any other form. Disable it and try using it again. //It likes to kill python scripts.

## How to ensure all cards ware downloaded
- to be sure that program downloaded all the cards you can use this formula: ((number of pages) - 1) * 24 + (number of cards on last page)
- for 7 pages, when last contains 4 cards it would loo like:  6*24+4 = 148 cards

