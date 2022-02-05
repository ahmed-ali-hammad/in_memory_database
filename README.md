# in_memory_database similar to Redis.

Use python version 3.10 or higher.

The script accepts both lower case and upper case commands.


The script accepts these commands: 

1- SET        (TO ADD A NEW RECORD), EXAMPLE 'SET a 20' 

2- UNSET      (TO DELETE A RECORD), EXAMPLE 'UNSET a' will delete this value

3- GET        (TO RETRIEVE A RECORD) 

4- NUMEQUALTO (PRINT out THE NUMBER OF VARIABLES THAT ARE SET TO A CERTAIN VALUE)

5- BEGIN      (OPENs A NEW TRANSACTION BLOCK) 

6- ROLLBACK   (UNDO ALL THE COMMANDS ISSUED IN THE MOST RECENT TRANSACTION BLOCK)

7- COMMIT     (CLOSE ALL THE TRANSACTION BLOCKS AND PERMANENTLY APPLY ALL THE CHANGES TO THEM)

8- END        (WILL EXIT THE PROGRAM)
