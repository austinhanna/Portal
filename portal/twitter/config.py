import configparser
config = configparser.ConfigParser()

# General Settings #
config['General'] = {}
config['General']['Keyword'] = 'Vape'

config['Auth'] = {}
config['Auth']['ckey'] = 'WEzuoWntc2NqKVg0FSnhlmDNR'
config['Auth']['csec'] = 'Rq4dcMN9gGo1JWaglibGUDqDLLPFpPkbQOhYlMSaJRfPcIjnuF'
config['Auth']['atok'] = '1905281930-DWTNXwF3F50Zu5zfbKEvKssuu9ejkbawHN06Tga'
config['Auth']['asec'] = '2GaOj1TTMGY2ZYEXkOOolZRipIyu9cdB41X5Bkj2W4UkA'

with open('config.ini', 'w') as configfile:
  config.write(configfile)
