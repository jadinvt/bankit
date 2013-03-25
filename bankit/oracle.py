from re import split, UNICODE

class Oracle():
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = self.build_index(self.transactions)

    def build_index(self, transactions):
        index = {}
        for transaction in transactions:
            for word in transaction.get_all_tags():
                if word in index:
                    index[word].append(transaction)
                else:
                    index[word] = [transaction,]
        return index
