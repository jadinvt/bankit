import ConfigParser
import os
import time

def main():
    BANKIT_DIR = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(BANKIT_DIR, os.pardir, 'conf', 'bankit.ini')
    #print(config_file)
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    
if __name__ == '__main__':
    print ("Running from command line")
    main()
