# # # # # # # # # # # # # # # # #
import configparser
import time
config = configparser.ConfigParser()
virgin = True
# # # # # # # # # # # # # # # # #


def configurator():
    if virgin == True:
        global time_en
        global weath_en
        global twit_en
        global news_en
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
        return u_name
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

    # # # # # # # # # # # # # # # # #

    ## Edit below this line! ##
    # General Settings #

    config['General']['FirstTime'] = 'ye'

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

    # Time Module #

    if time_en == True:
        config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
        config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.
        #config['Time Module']['other_time'] = ''
    else:
        config['Time Module']['local_time'] = 'Disabled'
        #config['Time Module']['get_from_system'] = 'Disabled' MAKE THIS SEPERATE...
    # Weather Module #

    if weath_en == True:
        config['Weather Module']['local_weather'] = 'Enabled'
        #config['Weather Module']['country_name'] = 'nil'
        #config['Weather Module']['city_name'] = 'nil'
    else:
        config['Weather Module']['local_weather'] = 'Disabled'

    # Twitter Module #
    if twit_en == True:
        config['Twitter Module']['twitter_live_feed'] = 'Enabled'
        config['Twitter Module']['live_feed_keyword'] = 'Enabled'
        config['Twitter Module']['live_feed_word'] = 'nil'
        config['Twitter Module']['live_feed_trending'] = 'Disabled'
        config['Twitter Module']['live_feed_people'] = 'Disabled'
        config['Twitter Module']['live_feed_person'] = '@nil'
    else:
        print('do something here') # live feed disable

    # News Module #
    if news_en == True:
        config['News Module']['news_ticker'] = 'Enabled'
        config['News Module'][''] = ''
    else:
        config['News Module']['news_ticker'] = 'Enabled'

    config['User Data']['Name'] = u_name

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
cunfig()
