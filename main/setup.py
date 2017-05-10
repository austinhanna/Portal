# # # # # # # # # # # # # # # # #
import configparser
import time
config = configparser.ConfigParser()
virgin = True # make obsolete
# # # # # # # # # # # # # # # # #

def configurator():
    if virgin == True:
        global time_en
        global weath_en
        global twit_en
        global news_en
        global reddit_en
        global subreddit
        global u_name

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
        print()
        twit_en = input('Would you like to enable the Twitter module?(True/False) ')
        print()
        news_en = input('Would you like to enable the News module?(True/False) ')
        print()
        reddit_en = input('Would you like to enable the Reddit module?(True/False) ')
        if reddit_en == 'True':
            print("Write subreddit as is do not write /r/.")
            subreddit = input("Which subreddit would you like to see headlines from? (Default /r/all) ")
        print()
        print('Writing to file...')
        time.sleep(1)
        print()
        print("DONE!")
        print()
        print('Configurator done.')

        ### Send 'em back! ###
        return time_en
        return weath_en
        return twit_en
        return news_en
        return reddit_en
        return u_name
        return subreddit
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
    config['News Module'] = {}
    config['Reddit Module'] = {}

    # # # # # # # # # # # # # # # # #

    # General Settings #
    config['General']['firstboot'] = 'Disable'
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
    config['Modules']['news_ticker'] = news_en
    config['Modules']['reddit'] = reddit_en

    # Time Module #
    config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
    config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.

    # Weather Module #
    config['Weather Module']['local_weather'] = 'Enabled'
    config['Weather Module']['country_name'] = 'nil'
    config['Weather Module']['city_name'] = 'nil'

    # Twitter Module #
    config['Twitter Module']['twitter_live_feed'] = 'Enabled'
    config['Twitter Module']['live_feed_keyword'] = 'Enabled'
    config['Twitter Module']['live_feed_word'] = 'nil'
    config['Twitter Module']['live_feed_trending'] = 'Disabled'
    config['Twitter Module']['live_feed_people'] = 'Disabled'
    config['Twitter Module']['live_feed_person'] = '@nil'

    # News Module #
    config['News Module']['news_ticker'] = 'Enabled'
    config['News Module'][''] = ''

    # Reddit Module #
    config['Reddit Module']['Active'] = 'nil'
    config['Reddit Module']['Subreddit'] = subreddit

    # User Data Module #
    config['User Data']['Name'] = u_name

    with open('bin/config.ini', 'w') as configfile:
        config.write(configfile)

cunfig()
