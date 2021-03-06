import os
import psutil

# blockchain is empty
blockchain = []


def get_last_blockchain_value():
    """ Returns the Last value of current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# default arguments in use
def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: the amount that should be added.
        :last_transaction: the last blockchain transaction (default [1]).
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input("Your transaction amount please: "))
    return user_input


def get_user_choice():
    user_input = input("Your Choice: ")
    return user_input


def print_blockchain_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        """block[0] is always the previous block"""
        print('Block in blockchain:', block[0])
        """blockchain[block_index - 1] is always the previous block"""
        print('Blockchain[block_index - 1]:', blockchain[block_index - 1])
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the Chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print("Input was invalid please pick a value from the list")
    if not verify_chain():
        print("Invalid Blockchain!")
        break

print("Done")
process = psutil.Process(os.getpid())
print("Memory:", process.memory_full_info().rss)
