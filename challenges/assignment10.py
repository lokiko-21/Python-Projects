def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1, var2
    

"""
PAY ATTENTION TO THE TRUE AND FALSE VALUES FOR "go" AS
THOSE ARE WHAT WILL KEEP ALLOWING THE USER TO TYPE INPUT
OVER AND OVER UNTIL THEY TYPE IN THE CORRECT VALUES!!!!
"""
def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except:
            print("\n\nOops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1, var2, var3))
        

if __name__ == "__main__":
    compute()
