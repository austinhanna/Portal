# Read config and import variables #
import configparser
cfg = configparser.ConfigParser()

cfg.read('config.ini')
print(cfg.sections())
