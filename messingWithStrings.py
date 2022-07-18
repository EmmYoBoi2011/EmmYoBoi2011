def main():
    x = "Welcome to Python my child!"
    print(x)
    print("Ooo! That was a string there!")
    print("Look what I can do with it!")
    y = input("Press ENTER to continue!")
    for i in x:
        print(i)
        y = input()
    print("Isn't it cool?")
    n = input('Edit the string! First you need to type x = "", and put you text of choice inside the quotes!\n')
    y = n.replace('"', "")
    z = y.split("= ")
    x = z[1]
    print("Let's use the print() method to display it!")
    print(x)
    def printing():
        y = input('Do it yourself! Type print() and put "x" (our string name) in the brackets! \n')
        if y == "print(x)":
            print(x)
            return
        else:
            print("Oops! That's wrong dear! Try again!")
            a = input("Press ENTER to continue!")
            printing()
    printing()
    print("Wonderful!")
    y = input('Press ENTER to continue!')
    print("How about we do what we did the other time?")
    def secondTask():
        print("For that we need to type: \nfor i in x: \n    print(i)")
        print("x is our string, i is... a character, I guess.")
        y = input("So, type it! \n")
        if y == "for i in x:":
            y = input()
        else:
            print("Be careful dear!")
            secondTask()
        if y == "    print(i)":
            y = input("Press ENTER to continue!")
            for i in x:
                print(i)
                y = input()
            return
        else:
            print("Be careful dear!")
            secondTask()
    secondTask()
    print("Brilliant!")
    print("Fun fact: the same way you edit strings, you can assign them!")
    print("Since you know that now, go over to onlinegdb.com/online_python_compiler and write some python code there!")
main()