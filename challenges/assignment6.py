import testModule
import datetime
import random

if __name__ == "__main__":
    results = testModule.getNumbers(5, 9)
    print(results)
    today = datetime.date(2023, 4, 19)
    print(today)
    #DISPLAYING RANDOM NUMBER BETWEEN 1 AND 10
    print(random.randrange(1,11))
