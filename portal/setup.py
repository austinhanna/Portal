import configparser
config = configparser.ConfigParser()

# General Settings #
config['GENERAL'] = {}
config['GENERAL']['FirstTime'] = 'True'

# Modules #
config['MODULES'] = {}
config['MODULES']['local_time'] = 'Enabled'
config['MODULES']['other_time'] = 'Disabled'
config['MODULES']['local_weather'] = 'Enabled'
config['MODULES']['other_weather'] = 'Disabled'
config['MODULES']['twitter_feed'] = 'Enabled'
#config['MODULES']['news_ticker'] = 'Enabled'

# Time Module #
config['Time Module'] = {}
config['Time Module']['local_time'] = 'Enabled' # Should stay enabled unless you want the current time on mars for some reason...
config['Time Module']['get_from_system'] = 'Enabled' # If enabled then the module will pull the current time from the PC rather than the internet. This can be reliable if there is no internet connection.
config['Time Module']['other_time'] = ''


# Weather Module #
config['Weather Module'] = {}
config['Weather Module']['local_weather'] = 'Enabled'
config['Weather Module']['country_name'] = 'nil'
config['Weather Module']['city_name'] = 'nil'

# Twitter Module #
config['Twitter Module'] = {}

# News Module #
#config['News Module'] = {}
#config['News Module']['news_ticker'] = 'Enabled'
#config['News Module'][''] = ''


# Placement Settings #
config['PLACEMENT'] = {}
config['PLACEMENT']['top_left'] = 'nil'
config['PLACEMENT']['top_right'] = 'nil'
config['PLACEMENT']['bottom_left'] = 'nil'
config['PLACEMENT']['bottom_right'] = 'nil'
config['PLACEMENT']['middle'] = 'nil'
config['PLACEMENT']['bottom'] = 'nil'

with open('config.ini', 'w') as configfile:
  config.write(configfile)
