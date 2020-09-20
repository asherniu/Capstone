import configparser

config = configparser.ConfigParser()
config.read('config.ini')
IEX_API = config['DEFAULT']['IEX_API']