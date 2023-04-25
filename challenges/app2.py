import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    #THE FOLLOWING IS CALING CODE FROM WITHIN THIS SCRIPT
    print("I am running code from {}".format(print_app2()))

    #THE FOLLOWING IS CALING CODE FROM THE IMPORTED app.py
    print("I am running code from {}".format(app.print_app()))
