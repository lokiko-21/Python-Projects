#GLOBAL SCOPR
name = "Python"

def getName():
    #LOCAL SCOPE
    name = "C#"
    print("I am coding with {}".format(name))

getName()

print("\n")

#this is a comment
"""
this is also used
to make comments, BUT
they can be longer!
"""
##using alt+3 also works to comment and un-comment

def printMe():
    """This is my docstring
    """

    print("Meeeeeee")

print(printMe.__doc__)
