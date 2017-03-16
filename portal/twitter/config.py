import configparser
config = configparser.ConfigParser()

# General Settings #
config['General'] = {}
config['General']['Keyword'] = 'Vape'

with open('config.ini', 'w') as configfile:
  config.write(configfile)
