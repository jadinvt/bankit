import unittest
import time
from re import split, UNICODE
from bankit.transaction import Transaction


class TransactionTest(unittest.TestCase):
    # 04/01/2012,"Check Card: MYO MASSAGE AUSTIN TX  03/30/12Card 16 #7343",-$100.00,$4709.40,
    def setUp(self):
        date = time.strptime("04/01/2012", "%m/%d/%Y")
        self.transaction = Transaction(date, "Check Card: MYO MASSAGE AUSTIN TX  03/30/12Card 16 #7343", -100, 4709.40)
        self.tags = split(r'\s+', "Check Card: MYO MASSAGE AUSTIN TX  03/30/12Card 16 #7343", UNICODE)

    def teardown_test(self):
        self.transaction = None

    def transaction_creation_test(self):
        self.assertTrue(self.transaction is not None)

    def add_tag_test(self):
        print set(self.transaction.get_tags())
        print set(self.tags)
        self.assertTrue(set(self.transaction.get_all_tags()) == set(self.tags))
        self.transaction.add_tag('test tag')
        self.tags.append('test tag')
        self.assertTrue(set(self.transaction.get_all_tags()) == set(self.tags))

    def get_date_test(self):
        self.assertTrue(self.transaction.get_date() == self.date)

    def set_date_test(self):
        transaction.set_
