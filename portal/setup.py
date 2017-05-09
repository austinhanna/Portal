# # # # # # # # # # # # # # # # #
import configparser
import time
config = configparser.ConfigParser()
virgin = True
# # # # # # # # # # # # # # # # #


def configurator():
    if virgin == True:
        config['User Data'] = {}

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
        time.sleep(1)
        print()
        ###

        ### User input ###
        u_name = input('What should I call you? ')
        print()
        time.sleep(.4)
        print('Hi, '+u_name+'!')
        print()


        
        ### Append configs ###
        config['User Data']['Name'] = u_name
        with open('userdata.ini', 'w') as configfile:
            config.write(configfile)
configurator()

def cunfig():
    # If you are making a module you can add it's config below. #
    # config['NAME'] = {}
    config['General'] = {}
    config['Placement'] = {}
    config['Modules'] = {}
    config['Time Module'] = {}
    config['Weather Module'] = {}
    config['Twitter Module'] = {}
    config['News Module'] = {}

    # # # # # # # # # # # # # # # # #

    ## Edit below this line! ##
    # General Settings #

    config['General']['FirstTime'] = 'True'

    # Placement Settings #

    config['Placement']['top_left'] = 'nil'
    config['Placement']['top_right'] = 'nil'
    config['Placement']['bottom_left'] = 'nil'
    config['Placement']['bottom_right'] = 'nil'
    config['Placement']['middle'] = 'nil'
    config['Placement']['bottom'] = 'nil'

    # Modules #

    config['Modules']['local_time'] = 'Enabled'
    config['Modules']['other_time'] = 'Disabled'
    config['Modules']['local_weather'] = 'Enabled'
    config['Modules']['other_weather'] = 'Disabled'
    config['Modules']['twitter_feed'] = 'Enabled'
    config['Modules']['news_ticker'] = 'Enabled'

    # Time Module #

    config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
    config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.
    #config['Time Module']['other_time'] = ''

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


    # Okay don't touch this either. #
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
