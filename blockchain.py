# blockchain is empty
blockchain = []


# Python code style guide: states 2 empty lines between function definitions
# Done for code reuse-ability purposes, each function has only one job
def get_last_blockchain_value():
    """ Returns the Last element of current blockchain"""
    return blockchain[-1]


# defaule arguments in use
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = float(input("Your transaction amount please: "))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
# Keyword arguments
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
