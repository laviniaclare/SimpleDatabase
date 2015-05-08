def simple_database():
    db = {}
    on = True
    while on:
        command = raw_input('--->').split(' ')
        if command[0] == 'END':
            on = False
        elif command[0] == 'SET':
            db[command[1]] = command[2]
        elif command[0] == 'GET':
            if command[1] in db:
                print db[command[1]]
            else:
                print 'NULL'
        elif command[0] == 'UNSET':
            if command[1] in db:
                del db[command[1]]
            else:
                print 'ITEM DOES NOT EXIST'
        elif command[0] == 'NUMEQUALTO':
            print db.values().count(command[1])
        elif command[0] == 'BEGIN':
            updates = transaction_block(db)
            if updates:
                db = updates
        elif command[0] == 'ROLLBACK':
            print 'NO TRANSACTION'
        else:
            print 'PLEASE ENTER A VALID COMMAND'


def transaction_block(db):
    temp_db = {}
    for item in db.keys():
        temp_db[item] = db[item]
    while True:
        command = raw_input('--->').split(' ')
        if command[0] == 'SET':
            temp_db[command[1]] = command[2]
        elif command[0] == 'GET':
            if command[1] in temp_db:
                print temp_db[command[1]]
            else:
                print 'NULL'
        elif command[0] == 'UNSET':
            if command[1] in temp_db:
                del temp_db[command[1]]
            else:
                print 'ITEM DOES NOT EXIST'
        elif command[0] == 'NUMEQUALTO':
            print temp_db.values().count(command[1])
        elif command[0] == 'BEGIN':
            updates = transaction_block(temp_db)
            if updates:
                temp_db = updates
        elif command[0] == 'ROLLBACK':
            break
        elif command[0] == 'COMMIT':
            return temp_db
        elif command[0] == 'END':
            print 'PLEASE COMMIT OR ROLLBACK TRANSACTION BEFORE EXITING PROGRAM'
        else:
            print 'PLEASE ENTER A VALID COMMAND'


if __name__ == '__main__':
    simple_database()
