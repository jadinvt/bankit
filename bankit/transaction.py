from re import split, UNICODE


class Transaction():
    # 04/01/2012,"Check Card: MYO MASSAGE AUSTIN TX  03/30/12Card 16 #7343",-$100.00,$4709.40,
    def __init__(self, date, description, amount, remaining_at_time):
        self.date = date
        self.description = description
        self.amount = amount
        self.remaining_at_time = remaining_at_time

        self.native_tags = split(r'\s+', description, UNICODE)
        self.human_tags = []

    def get_all_tags(self):
        return self.native_tags + self.human_tags

    def add_tag(self, tag):
        self.human_tags.append(tag)

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_remaining(self):
        return self.remaining

    def set_remaining(self, amount):
        self.remaining_at_time = amount
