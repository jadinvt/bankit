import os
import sys
import re
import time
import ConfigParser
import argparse
import pickle
from transaction import Transaction


def main():
    data_file = ''
    BANKIT_DIR = os.path.dirname(os.path.abspath(__file__))
    args = get_args()
    if args.config:
        config = get_config(BANKIT_DIR, args.config)
    else:
        config = get_config(BANKIT_DIR)
    if args.pickle:
        pickle_file = args.pickle
    elsif config.get('DEFAULT', 'pickle_file'):
        pickle_file = os.path.join(BANKIT_DIR, '..', config.get('DEFAULT', 'data_dir'), config.get('DEFAULT', 'pickle_file'))
    else:
        
    if args.read:
        if args.data:
            data_file = args.data
        else:
            data_file = os.path.join(BANKIT_DIR, '..', config.get('DEFAULT', 'data_dir'), config.get('DEFAULT', 'data_file'))
        read_data(data_file)
    else:
        print "reading and interacting"
    print data_file


def read_data(data_file):
    fd = open(data_file, 'r')
    line = fd.readline()
    transactions = []
    while line:
        print line
        search_result = re.search(r'(\d{2}/\d{2}/\d{4}),"(.*)",(-?\$?\d+\.\d{2}?),(-?\$?\d+\.\d{2}?)', line)
        if not search_result:
            search_result = re.search(r'(\d{2}/\d{2}/\d{4}),(.*),(-?\$?\d+\.\d{2}?),(-?\$?\d+\.\d{2}?)', line)
        date = time.strptime(search_result.group(1), "%m/%d/%Y")
        description = search_result.group(2)
        amount = search_result.group(3)
        remaining_amount = search_result.group(4)
        transactions.append(Transaction(date, description, amount, remaining_amount))
        line = fd.readline()
    with open('transactions.pickle', 'wb') as file:
        pickle.dump(transactions, file)


def get_config(root_dir, config_file=''):
    if not config_file:
        config_file = os.path.join(root_dir, os.pardir, 'conf', 'bankit.ini')
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    return config


def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-r', '--read', help='Read in data file', action='store_true', )
    parser.add_argument('-c', '--config', help='Specify config file')
    parser.add_argument('-d', '--data',  help='Specify data file')
    parser.add_argument('-p', '--pickle',  help='Specify pickle file')
    return parser.parse_args()


if __name__ == '__main__':
    print ("Running from command line")
    main()
