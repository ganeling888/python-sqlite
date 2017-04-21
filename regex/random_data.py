## Define the flavors that may be used as an ice cream
flavor_type = { 'strawberry', 'vanilla', 'chocolate', 'banana', }
## Define the types of dishes that can be served
dish_type = { 'cone', 'cup', 'dish'}
## Define the available options for the purchasing options
purchasing_type = { 'single', 'double', 'triple' }

import random
import csv

## More information about random library here
# https://docs.python.org/2/library/random.html


# Returns a random string corresponding to float x from 1 to 100
def randomPrice():
    return scrambler(str(random.uniform(1, 100)))

# Returns a random dish corresponding to an item from list dish
def randomDish():
    return scrambler(random.sample(dish_type, len(dish_type))[random.randint(0, len(dish_type)-1)])

# Returns a random flavor corresponding to an item from list flavor
def randomFlavor():
    return scrambler(random.sample(flavor_type, len(flavor_type))[random.randint(0, len(flavor_type)-1)])

# Returns a random purchasing_type corresponding to an item from list purchasing_type
def randomPurchase():
    return scrambler(random.sample(purchasing_type, len(purchasing_type))[random.randint(0, len(purchasing_type)-1)])

def chaos():
    # ~10% chance
    if (random.random() * 100 >= 95):
        return random.random() + chaos()
    # ~5% chance
    elif (random.random() * 100 >= 90):
        return chaos() + random.random() + chaos()
    # ~25% chance
    elif (random.random() * 100 >= 75):
        return chaos() + random.random()
    # ~75% chance
    else:
        return random.random()
def scrambler(normal):
    # Concat the normal string with some random data
    insane = normal + str(chaos())
    # ~10% chance
    if (random.random() * 100 >= 90):
        # Pick a random sampling from the insane scrambled string
        return ''.join(random.sample(insane,len(insane)))
    # ~25% chance
    if (random.random() * 100 >= 75):
        # Just return the concat'd string
        return insane
    else:
        # Don't mess with the data
        return normal
def writeOutRandomData():
    import csv
    import random
    import faker

    fake = faker.Faker()


    with open('ice_cream.csv', 'w') as csvfile:
        # Define the column names for the CSV
        fieldnames = ['price', 'flavor_type', 'dish_type', 'purchasing_type', 'transaction_date']
        # Set up the DictWriterclass
        ## https://docs.python.org/2/library/csv.html#csv.DictWriter
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(500):
            # Generate a random datetime from faker
            rand_date = fake.date_time()
            # Write out some random data, and generate an isoformated datetime
            writer.writerow( {'price': randomPrice(), 'dish_type': randomDish(), 'purchasing_type': randomPurchase(), 'flavor_type': randomFlavor(), 'transaction_date':  rand_date.isoformat() })

def getTransactionTimeFromTimestamp(timestamp):
    import re
    shortenedTimestamp  = timestamp.split("T",1)[1]
    result = re.match('[0-9]{2}:[0-9]{2}:[0-9]{2}',shortenedTimestamp)
    return result.group()

def getTransactionDateFromTimestamp(datetime):
    import re
    shortenedDatetime = datetime.split("T",0)[0]
    result = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}',shortenedDatetime)
    return result.group()
def checkForIntegerSpaceThenString(string):
    import re
    result = re.match('[0-9]+\s*[a-zA-Z]+',string)
    return bool(result)

def checkForExistenceInSubstring(string, substring):
    return bool(string in substring)

def validateDecimalTransaction(string, n, m):
    import re
    print("Checking that string " + string + " has " + str(n) + " digits preceding decimal and " + str(m) + " digits following decimal.")
    result = re.search('[0-9]{' + str(n) + '}.[0-9]{' + str(m) + '}', string)
    return bool(result)

def padIntegerStringWithNZero(tobepadded,n):
    import re
    print("Padding the string " + tobepadded + " with " + str(n-len(tobepadded)) + " zeros.")
    while (re.match('[0-9]{' + str(n) + '}',str(tobepadded)) == None):
        tobepadded = "0" + str(tobepadded)
    return tobepadded

def main():
    print(padIntegerStringWithNZero("123",10))
    print(validateDecimalTransaction("12.30",2,2))
    print(checkForExistenceInSubstring("cup","cup0.992967744665"))
    print(checkForIntegerSpaceThenString("75 MG"))
    print(getTransactionTimeFromTimestamp("1996-05-21T19:27:10"))
    print(getTransactionDateFromTimestamp("1996-05-21T19:27:10"))

if __name__ == "__main__":
    main()
