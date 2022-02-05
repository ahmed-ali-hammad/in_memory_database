# Instructions:
# Please use python version 3.10 or higher.
# to activate the database, Please open the terminal in the same folder as the script then run this command 'python in_memory_database.py'.
# the script accepts both lower case and upper case commands.

# The script accepts these commands: 
# 1- SET        (TO ADD A NEW RECORD), EXAMPLE 'SET a 20' 
# 2- UNSET      (TO DELETE A RECORD), EXAMPLE 'UNSET a' will delete this value
# 3- GET        (TO RETRIEVE A RECORD) 
# 4- NUMEQUALTO (PRINT out THE NUMBER OF VARIABLES THAT ARE SET TO A CERTAIN VALUE)  
# 5- BEGIN      (OPENs A NEW TRANSACTION BLOCK) 
# 6- ROLLBACK   (UNDO ALL THE COMMANDS ISSUED IN THE MOST RECENT TRANSACTION BLOCK)
# 7- COMMIT     (CLOSE ALL THE TRANSACTION BLOCKS AND PERMANENTLY APPLY ALL THE CHANGES TO THEM)
# 8- END        (WILL EXIT THE PROGRAM) 


# Welcome Message
print('The database is currently activated, please use one of the appropriate commands')

# Main Function
def in_memory_database():
    transaction_blocks = [{'commited' : False}]

    while (user_input := input('->')).split()[0].lower() != 'end':
        command = user_input.split()
        match command[0].lower(): # Match case is used instead of if else statement
            case 'set':
                transaction_blocks[-1][command[1]] = command[2]
            case 'unset':
                del transaction_blocks[-1][command[1]]
            case 'get':
                try:
                    print(transaction_blocks[-1][command[1]])
                except:
                    print('NULL')
            case 'numequalto':
                print(list(transaction_blocks[-1].values()).count(command[1]))
            case 'begin':
                if transaction_blocks == [{'commited' : False}]:
                    pass
                else:
                    new_transaction_block = transaction_blocks[-1].copy()
                    transaction_blocks.append(new_transaction_block)
            case 'rollback':
                if transaction_blocks[-1]['commited'] == True or transaction_blocks == [{'commited' : False}]:
                    print('NO TRANSACTION')
                elif len(transaction_blocks) == 1:
                    rolled_back_transaction_blocks = [ transaction_block.update((k,'NULL') for k in transaction_block) for transaction_block in transaction_blocks ]
                    transaction_blocks[-1]['commited'] = False
                else:
                    transaction_blocks.pop()
            case 'commit':
                if transaction_blocks[-1]['commited'] == True or transaction_blocks == [{'commited' : False}]:
                    print('NO TRANSACTION')
                else:   
                    commited_transaction_blocks = [ transaction_block.update(commited = True) for transaction_block in transaction_blocks ]
            case _:
                print('Please use one of the appropriate commands')

# executing the function
if __name__ == "__main__":
    in_memory_database()
        