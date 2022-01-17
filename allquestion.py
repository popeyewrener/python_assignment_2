
'''HELLO GUYS TO THE PROGRAM
   EVERY PROGRAM ARE MADE INTO FUNCTIONS AND CALLED LATER ON IN FORM OF
    OPTIONS!!!
    THANKS FOR THE ASSIGNMENT, I LEARNT A LOT BY DOING THESE!!



    Program by CHAITANYA KANHAR CSE 21103127
    '''


inject=''

def q1():
    input_string=input("Enter the string:(Leave blank for default) ") or "Python is a case sensitive language"  
    #part a
    print("Part A!")
    print("Length os input string",len(input_string))
    print("Part B!")
    print("Reverse of string is","'"+input_string[-1: :-1]+"'")
    print("Part C!")
    slicestr=input_string[slice(9,26)]
    print(slicestr)
    print("Part D!")
    newstring=input_string.replace("a case sensitive","object oriented")
    print(newstring)
    print("Part E")
    print("Index of substring 'a' is",input_string.index('a') )
    print("Part F!")
    print(input_string.replace(" ",""))
    finchoice()

def q2():
    name=input("Please enter your name: ")
    sid=input("Enter SID: ")
    dep=input("Enter department name: ")
    cgpa=float(input("Enter CGPA: "))
    print('''
    ''')
    print('''Hey, %s Here!
             My SID is %s
             I am from %s department and my CGPA is %s'''%(name,sid,dep,cgpa))
    finchoice()


def q3():
    a=56
    b=10
    print("Part A!")
    print("a&b: ",a&b)
    print(" ")
    print("Part B!")
    print("a|b: ",a|b)
    print(" ")
    print("Part C!")
    print("a^b: ",a^b)
    print(" ")
    print("Part D!")
    print("a<<2:",a<<2,"and", "b<<2: ",  b<<2)
    print(" ")
    print("Part E!")
    print("a>>2:",a>>2, "and b>>4",b>>4)
    finchoice()
def q4():
    l=[]
    for i in range(3):
        num=float(input("Enter number %s: "%(i+1)))
        l.append(num)

    l.sort(reverse=True)
    print("The greatest value is:",l[0])
    finchoice()

def q5():
    inp_string=input("Enter the string: ")
    if 'name' in inp_string:
        print("yes")

    else:
        print("no") 
    finchoice()    


def q6():
    sides=[]
    for i in range(3):
        side=float(input("Enter side %s: "%(i+1)))
        sides.append(side)
    finchoice()


    def qmethod():
        #Question paper's method
        print("Question paper's method!!")
        if sides[0]>sides[1]+sides[2] or sides[1]>sides[2]+sides[0] or sides[2]>sides[0]+sides[1]:
            print("No")
            
        else:
            print("Yes")   

        finchoice()     


    def mymethod():
        #My method
        sides.sort()
        if sides[2]>sides[1]+sides[0]:
            print("No")
        else:
            print("Yes")

        finchoice()    
    def choicecq():
        print('''Input 1 for Question paper's logic
        Input 2 for myy simple logic!''')
        usrchoice=input("Choose the method you want to use:")
        if usrchoice=='1':
            qmethod()
        elif usrchoice=='2':
            mymethod()

        else:
            print("Entered wrong choice")
            print("Taking you to choice again!!!")
            choicecq()   


    choicecq()         
        
        

def choice():     
    try:
        print("Program by CHAITANYA KANHAR CSE 21103127")
        print("WELCOME to the program %s.\n Hope it will help"%(inject))
        print("Choose the question want to visit: input are set as (1,2,3,4,5,6)!!")   
        inpchoice=input("Enter your choice here: ")
        if inpchoice == '1':
            q1()
        elif inpchoice == '2':
            q2()
        elif inpchoice == '3':
            q3()
        elif inpchoice == '4':
            q4()
        elif inpchoice == '5':
            q5()
        elif inpchoice == '6':
            q6()
        else:
            print("Wrong input")
            print('Taking you to choice')
            choice()                        

        

    except ValueError:
        print("You have got an value error or typed wrong value!!!")
        print("Taking you back to choice!!!")
        choice()

def finchoice():
    print("You want to try more or exit??")
    finc=input("'Y' for yes, 'N' for no ")
    if finc.upper()=='Y':
        global inject
        inject ='again'
        choice()

    elif finc.upper()=='N':
        print("Program exited")
        print("Thanks for using!!")   

    else:
        print("Wrong choice. Try again")
        print("Taking to previous choice")
        finchoice()     


        


choice()        
