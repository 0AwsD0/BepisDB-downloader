from download import download

def menu():
    #make cfg file or txt that allows to automaticaly select option
    print("BepisDB Card Downloader - select type of card to download (enter number or use config file):")
    print("1. KK")
    print("2. AA2")
    print("3. HS")
    print("4. PH")
    print("5. AI/HS2")
    print("6. COM3D2")
    print("7. SH")
    print("8. HC")

    selected = input()

    #make cfg file or txt that allows to automaticaly or skit + defaults are just empty- write it into documentation
    #for all of em like KK AA2 for example - kk.txt -> contains setings for that one | AA2.txt -> contains settings for that one / if the row isblank the user inoputs the data here like -> tags = long_hair; name = ; <- will be prompted toinsert name in consoleor click enter to set default
    if selected == "1":
        game = "KK"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            KK(game)
        else:
            basic(game)
    elif selected == "2":
        game = "AA2"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            AA2_and_AI_HS2(game)
        else:
            basic(game)
    elif selected == "3":
        game = "HS"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            HS(game)
        else:
            basic(game)
    elif selected == "4":
        game = "PH"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            PH(game)
        else:
            basic(game)
    elif selected == "5":
        game = "AI_HS2"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            AA2_and_AI_HS2(game)
        else:
            basic(game)
    elif selected == "6":
        game = "COM3D2"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            COM3D2(game)
        else:
            basic(game)
    elif selected == "7":
        game = "SH"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            SH(game)
        else:
            basic(game)
    elif selected == "8":
        game = "HC"
        print("If you wish to enter only name and/or tags press 1 or ENTER (or anything else really). For advance download press 2.")
        selected = input()
        if selected == "2":
            HC(game)
        else:
            basic(game)
    else:
        print("Please select one of the correct options (1-6):")
        main()


def KK(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    gender = input()
    print("Personality: (text) <Default> = Unspecified")
    personality = input()
    print("Gametype: (text) <Default> = Unspecified")
    game_type = input()
    print("Does bit contain modded content: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    modded_content = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, gender = gender, personality = personality, game_type = game_type, modded_content = modded_content, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)


def AA2_and_AI_HS2(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    gender = input()
    print("Personality: (text) <Default> = Unspecified")
    personality = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, gender = gender, personality = personality, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)

def HS(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    gender = input()
    print("Personality: (text) <Default> = Unspecified")
    personality = input()
    print("Gametype: (text) <Default> = Unspecified")
    game_type = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, gender = gender, personality = personality, game_type = game_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)


def PH(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)

def COM3D2(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Preset type: (text) <Default> = Unspecified")
    preset_type = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, preset_type = preset_type, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)


def SH(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)

def HC(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    print("Gender: (text) <Default> = Unspecified")
    gender = input()
    print("Order by: (enter 1 for 'Date Descending' <Default> | 2 for 'Date Ascending' | 3 for 'Popularity')")
    order_by = input()
    print("Show hidden: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_hidden = input()
    print("Show only featured: (checkbox - enter '1' to check - 0 or nothig to leave unchecked <Default>)")
    show_only_featured = input()
    download(game = game, name = name, tags = tags, gender = gender, order_by = order_by, show_hidden = show_hidden, show_only_featured = show_only_featured)

def basic(game):
    print("Enter in order (or use config file) the parameters or press enter to set default.")
    print("Name: (text) <Default> = blank")
    name = input()
    print("Tags: (text) <Default> = blank")
    tags = input()
    download(mode="basic", game=game, name=name, tags=tags)

def main():
    menu()

if __name__ == "__main__":
    main()
