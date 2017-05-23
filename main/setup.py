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
    ###

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

    print()
    ssh_en = input('Would you like to enable SSH? (True/False) ')
    if ssh_en == 'True' or ssh_en == 'T' or ssh_en == 'Y':
        print()
        ssh_user = input("Write your *NEW* username. (Note: Default is magic) ")
        ssh_pass = input("Write your *NEW* password. (Note: Default is mirror) ")
    print()
    print('Writing to file...')
    time.sleep(1)
    print()
    print("DONE!")
    print()

    ### Send 'em back! ###
    return time_en
    return weath_en
    return twit_en
    return reddit_en
    return u_name
    return subreddit
    return ckey
    return csec
    return atok
    return asec
    return keyword
    return city
    return owm_api_key
    return unit
    return ssh_user
    return ssh_pass
configurator()

def cunfig():
    # If you are making a module you can add it's config below. #
    # config['NAME'] = {}
    config['General'] = {}
    config['User Data'] = {}
    config['Placement'] = {}
    config['Modules'] = {}
    config['Time Module'] = {}
    config['Weather Module'] = {}
    config['Twitter Module'] = {}
    config['Twitter Auth'] = {}
    config['Reddit Module'] = {}

    # # # # # # # # # # # # # # # # #

    # General Settings #
    config['General']['firstboot'] = 'Disable'
    config['General']['SSH Username'] = ssh_user
    config['General']['SSH Password'] = ssh_pass
    # Placement Settings #

    config['Placement']['top_left'] = 'nil'
    config['Placement']['top_right'] = 'nil'
    config['Placement']['bottom_left'] = 'nil'
    config['Placement']['bottom_right'] = 'nil'
    config['Placement']['middle'] = 'nil'
    config['Placement']['bottom'] = 'nil'

    # Modules #

    config['Modules']['time'] = time_en
    config['Modules']['weather'] = weath_en
    config['Modules']['twitter_feed'] = twit_en
    config['Modules']['reddit'] = reddit_en

    # Time Module #
    config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
    config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.

    # Weather Module #
    config['Weather Module']['local_weather'] = 'Enabled'
    config['Weather Module']['city_name'] = city
    config['Weather Module']['units'] = unit
    config['Weather Module']['apikey'] = '40460bd21017b5384bdfcbf78da21cc8'


    # Twitter Module #
    config['Twitter Module']['twitter_live_feed'] = 'Enabled'
    config['Twitter Module']['keyword'] = keyword
    config['Twitter Module']['live_feed_word'] = 'nil'
    config['Twitter Module']['live_feed_trending'] = 'Disabled'
    config['Twitter Module']['live_feed_people'] = 'Disabled'
    config['Twitter Module']['live_feed_person'] = '@nil'

    # Twitter Auth #
    config['Twitter Auth']['ckey'] = ckey
    config['Twitter Auth']['csec'] = csec
    config['Twitter Auth']['atok'] = atok
    config['Twitter Auth']['asec'] = asec

    # Reddit Module #
    config['Reddit Module']['Active'] = 'nil'
    config['Reddit Module']['Subreddit'] = subreddit

    # User Data Module #
    config['User Data']['Name'] = u_name

    with open('bin/config.ini', 'w') as configfile:
        config.write(configfile)

cunfig()
