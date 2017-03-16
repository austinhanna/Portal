# DO NOT TOUCH THESE. #
import configparser
config = configparser.ConfigParser()
config['General'] = {}
config['Auth'] = {}
########################


## Edit below this line! ##

# Which keyword would you like to show tweets from?
config['General']['Keyword'] = 'Python' # Show tweets by keyword
#config['General']['Trend'] = '#Python' -- To be added soon, Show tweets by trend
#config['General']['Person'] = '@Python' -- To be added soon, Show tweets by person
#blacklist = ['enter words that tweets may contain you don't want to see...'] # This will filter any tweet that has any keyword in it. Opposite of the Keyword setting above.
#config['General']['blacklist'] = '@Python' -- To be added soon, Show tweets by person

# Twitter API Auth codes. Keep these secret!
config['Auth']['ckey'] = 'WEzuoWntc2NqKVg0FSnhlmDNR' # Client Key
config['Auth']['csec'] = 'Rq4dcMN9gGo1JWaglibGUDqDLLPFpPkbQOhYlMSaJRfPcIjnuF' # Client Secret
config['Auth']['atok'] = '1905281930-DWTNXwF3F50Zu5zfbKEvKssuu9ejkbawHN06Tga' # Access Token
config['Auth']['asec'] = '2GaOj1TTMGY2ZYEXkOOolZRipIyu9cdB41X5Bkj2W4UkA' # Access Secret

with open('config.ini', 'w') as configfile:
  config.write(configfile)
