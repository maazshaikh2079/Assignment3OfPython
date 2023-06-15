# Info:-
# Name : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-3
# Topic  : WAP to create a simple calculator
# Date   : 15-06-2023

# Program:-
# Start function:-
def Start():
    n1=float(input("Enter number   : "))
    op=input("Enter operator : ")
    n2=float(input("Enter number   : "))
    print("Result:-")
    match op:
        case '+':
            print(n1,op,n2,"=",(n1+n2));
        case '-':
            print(n1,op,n2,"=",(n1-n2));
        case '*':
            print(n1,op,n2,"=",(n1*n2));
        case '/':
            print(n1,op,n2,"=",(n1/n2));
        case '%':
            print(n1,op,n2,"=",(n1%n2));
        case _ if(op=="**" or op=='^'):
            print(n1,op,n2,"=",(n1**n2));
        case '//':
            print(n1,op,n2,"=",(n1//n2));
        # Note: There will be ".0" after numbers due to float data type
        case '!':
            fact=1; i=1;  
            while(i<=n1):
                fact=fact*i
                i+=1;
            print(n1,op,n2,"=",(fact*n2));
        case _:
            print("Invalid operator!");
    print();

# Exit function:-
def Exit():
    print("exiting...")
    print();

# Driver code:-
ch=1;
print("_________________________");
print("|___SIMPLE_CALCULATOR___|");
print("| 1- Start              |");
print("| 2- Exit               |");
print("|_______________________|");
print();
while(ch!=2):
    ch=int(input("Enter your choice: "))
    print()
    match ch:
        case 1:
            Start();
        case 2:
            Exit(); 
        case _:
            print("Invalid choice!")
            print();

# Ouput:-
# _________________________
# |___SIMPLE_CALCULATOR___|
# | 1- Start              |
# | 2- Exit               |
# |_______________________|

# Enter your choice: 1

# Enter number   : 1
# Enter operator : +
# Enter number   : 4
# Result:-
# 1.0 + 4.0 = 5.0    

# Enter your choice: 1

# Enter number   : 2
# Enter operator : -
# Enter number   : 4
# Result:-
# 2.0 - 4.0 = -2.0   

# Enter your choice: 1

# Enter number   : 4
# Enter operator : *
# Enter number   : 5
# Result:-
# 4.0 * 5.0 = 20.0

# Enter your choice: 1

# Enter number   : 10
# Enter operator : /
# Enter number   : 2
# Result:-
# 10.0 / 2.0 = 5.0

# Enter your choice: 1

# Enter number   : 10
# Enter operator : %
# Enter number   : 3
# Result:-
# 10.0 % 3.0 = 1.0

# Enter your choice: 1

# Enter number   : 5
# Enter operator : ** 
# Enter number   : 2
# Result:-
# 5.0 ** 2.0 = 25.0

# Enter your choice: 1

# Enter number   : 5
# Enter operator : ^
# Enter number   : 2
# Result:-
# 5.0 ^ 2.0 = 25.0

# Enter your choice: 1

# Enter number   : 10
# Enter operator : //
# Enter number   : 2
# Result:-
# 10.0 // 2.0 = 5.0      # Note: ".0" due to float data type.

# Enter your choice: 1     

# Enter number   : 5
# Enter operator : !
# Enter number   : 1
# Result:-
# 5.0 ! 1.0 = 120.0  

# Enter your choice: 1

# Enter number   : 5
# Enter operator : !
# Enter number   : 2
# Result:-
# 5.0 ! 2.0 = 240.0  

# Enter your choice: 1

# Enter number   : 3
# Enter operator : #
# Enter number   : 7
# Result:-
# Invalid operator!

# Enter your choice: 3

# Invalid choice!

# Enter your choice: 2

# exiting...