# # # # # # # # # # # # # # # # #
import configparser
import time
config = configparser.ConfigParser()
# # # # # # # # # # # # # # # # #

def configurator():
    global time_en
    global weath_en
    global twit_en
    global reddit_en
    global subreddit
    global limit
    global client_id
    global client_sec
    global uagent
    global u_name
    global ckey
    global csec
    global atok
    global asec
    global keyword
    global city
    global owm_api_key
    global unit
    global ssh_user
    global ssh_pass

    ### Begin Info ###
    print('Running Configurator...')
    time.sleep(1)
    print()
    print()
    time.sleep(1)
    print('Welcome to the "Portal" Mirror Setup')
    time.sleep(1)
    print("This program will help you setup everything you need to get your mirror customised to your needs.")
    time.sleep(1)
    print("First, we will ask some simple questions.")
    time.sleep(3)
    print()

    ### User input ###
    u_name = input('What should I call you? ')
    print()
    time.sleep(.4)
    print('Hi, '+u_name+'!')
    print()

    print("Module Setup")
    time.sleep(3)
    print("Please answer each with a True/False")
    time.sleep(2)
    print()

    time_en = input('Would you like to enable the Time module?(True/False) ')
    print()

    weath_en = input('Would you like to enable the Weather module?(True/False) ')
    if weath_en == 'True' or weath_en == 'true' or weath_en == 't' or weath_en == 'T':
        print("")
        city = input('For which City/Town do you want to see weather from? ')
        unit = input('Celsius or Fareinheit? (C/F) ')
        owm_api_key = input('OWM API Key? ')
    else:
        city = 'nil'
        unit = 'nil'
        owm_api_key = 'nil'
    print()

    twit_en = input('Would you like to enable the Twitter module?(True/False) ')
    if twit_en == 'True':
        print("Paste keys as is and make sure there's no extra spaces!")
        ckey = input("First we need your client key: ")
        csec = input("Next, we need your client secret: ")
        atok = input("Then, we need your access token: ")
        asec = input("Finally, we need your access secret: ")
        keyword = input("What tweets do you want to see? (Just a word or hashtag a tweet might contain, Like 'Vape')")
        print("")
        print("Thanks!")
        time.sleep(1)
    else:
        ckey = 'nil'
        csec = 'nil'
        atok = 'nil'
        asec = 'nil'
        keyword = 'nil'
    print()

    reddit_en = input('Would you like to enable the Reddit module?(True/False) ')
    if reddit_en == 'True':
        print("Write subreddit as is do not write /r/.")
        subreddit = input("Which subreddit would you like to see headlines from? (Default /r/all) ")
        limit = input("How many posts would you like to see? ")
        print('Now we need your Client ID and Secret, along with a name for us. You can get this off the settings page and find your API key')
        uagent = input('(We reccomend just "Portal")Name: ')
        client_id = input('(NOT YOUR /u/)Client ID: ')
        client_sec = input('(OR YOUR PASSWORD.)Client Secret: ')
    else:
        subreddit = 'nil'
        limit = 'nil'
        uagent = 'nil'
        client_id = 'nil'
        client_sec = 'nil'
    print()

    ssh_en = input('Would you like to change SSH details? (True/False) ')
    if ssh_en == 'True' or ssh_en == 'T' or ssh_en == 'Y':
        print()
        ssh_user = input("Write your *NEW* username. (Note: Default is magic) ")
        ssh_pass = input("Write your *NEW* password. (Note: Default is mirror) ")
    else:
        ssh_user = 'nil'
        ssh_pass = 'nil'
    print()

    print('Writing to file...')
    time.sleep(1)
    print("DONE!")
    print()

    ### Send 'em back! ###
    return time_en
    return weath_en
    return twit_en
    return reddit_en
    return ssh_en

    return u_name
    return subreddit
    return limit
    return uagent
    return client_id
    return client_sec

    return ckey
    return csec
    return atok
    return asec
    return keyword

    return unit
    return city
    return owm_api_key

    return ssh_user
    return ssh_pass
configurator()

def cunfig():
    # If you are making a module you can add it's config below. #
    # config['NAME'] = {}
    config['General'] = {}
    config['User Data'] = {}
    config['Placement'] = {}
    config['Time Module'] = {}
    config['Weather Module'] = {}
    config['Twitter Module'] = {}
    config['Twitter Auth'] = {}
    config['Reddit Module'] = {}

    # # # # # # # # # # # # # # # # #

    # User Data Module #
    config['User Data']['Name'] = u_name
    # # # # # # # # # #

    # General Settings #
    config['General']['firstboot'] = 'Disable' # Disable this so we don't cuck it.
    config['General']['SSH Username'] = ssh_user # RPI?
    config['General']['SSH Password'] = ssh_pass
    # # # # # # # # # #

    # Placement Settings #
    config['Placement']['top_left'] = 'nil'
    config['Placement']['top_right'] = 'nil'
    config['Placement']['bottom_left'] = 'nil'
    config['Placement']['bottom_right'] = 'nil'
    config['Placement']['middle'] = 'nil'
    config['Placement']['bottom'] = 'nil'

    # Time Module #
    if time_en == 'True' or 'Y' or 'Yes':
        config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
        #config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.
    elif time_en == 'False' or 'N' or 'No':
        config['Time Module']['local_time'] = 'Disabled'
    # # # # # # # # # #

    # Weather Module #
    if weath_en == 'True' or 'Y' or 'Yes':
        config['Weather Module']['local_weather'] = 'Enabled'
    elif weath_en == 'False' or 'N' or 'No':
        config['Weather Module']['local_weather'] = 'Disabled'
    else:
        config['Weather Module']['local_weather'] = 'Enabled'
    config['Weather Module']['city_name'] = city
    config['Weather Module']['units'] = unit
    config['Weather Module']['apikey'] = '40460bd21017b5384bdfcbf78da21cc8'
    # # # # # # # # # #

    # Twitter Module #
    if twit_en == 'True' or 'Y' or 'Yes':
        config['Twitter Module']['twitter_live_feed'] = 'Enabled'
    elif twit_en == 'False' or 'N' or 'No':
        config['Twitter Module']['twitter_live_feed'] = 'Disabled'
    else:
        config['Twitter Module']['twitter_live_feed'] = 'Enabled'

    config['Twitter Module']['keyword'] = keyword
    config['Twitter Module']['live_feed_word'] = 'nil'
    config['Twitter Module']['live_feed_trending'] = 'Disabled'
    config['Twitter Module']['live_feed_people'] = 'Disabled'
    config['Twitter Module']['live_feed_person'] = '@nil'

    config['Twitter Auth']['ckey'] = ckey
    config['Twitter Auth']['csec'] = csec
    config['Twitter Auth']['atok'] = atok
    config['Twitter Auth']['asec'] = asec
    # # # # # # # # # #

    # Reddit Module #
    if reddit_en == 'True' or 'Y' or 'Yes':
        config['Reddit Module']['Enabled'] = 'Enabled'
    elif reddit_en == 'False' or 'F' or 'no' or 'n':
        config['Reddit Module']['Enabled'] = 'Disabled'
    else:
        config['Reddit Module']['Enabled'] = 'Enabled'

    config['Reddit Module']['Subreddit'] = subreddit
    config['Reddit Module']['Limit'] = limit
    config['Reddit Module']['PrjName'] = uagent
    config['Reddit Module']['Client ID'] = client_id
    config['Reddit Module']['Client Password'] = client_sec
    # # # # # # # # # #

    with open('bin/config.ini', 'w') as configfile:
        config.write(configfile)

cunfig()
