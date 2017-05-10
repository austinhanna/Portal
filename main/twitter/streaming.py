# Tweepy Imports #
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import json
import time
import configparser

# Config Parser
cfg = configparser.ConfigParser()

# Twitter Auth Codes #
cfg.read('config.ini')
ckey = cfg.get('Auth', 'ckey')
csecret = cfg.get('Auth', 'csec')
atoken = cfg.get('Auth', 'atok')
asecret = cfg.get('Auth', 'asec')

#enabled = cfg.get('Twitter Module', 'Enabled')
#if
