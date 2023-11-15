'''A simple calculator application which asks the user to select one of two options for input:
1) A text file with equations
2) Enter two numbers and an operator 
and print out all of the equations into a new text file with results.'''
while True:
    while True:
        try:
            option = int(input('''Please select an option for input:
                1) Text file
                2) Two numbers and an operator\n'''))
        except ValueError:
            print("Please enter only numbers 1 or 2.")  
            break
# Taking input as text file and printing the equations into another text file            
        while True:
            if option == 1:
                try:
                    input_text_file = input("Please enter the name of the text file you would like to give as input with .txt at the end:\n")
                    with open(input_text_file, "r") as input_file:
                        entry_data = input_file.readlines()
                        print(entry_data)
# A new file is created to collect the output                        
                    f = open("Task 9_simple_calc.txt",'a')
                    f.writelines(entry_data) 
                    f.close()
                    break      
                except FileNotFoundError:
                    print("Please enter the correct file name with .txt extension.")
# Taking two numbers and operator as an input.                         
            elif option == 2: 
                try:
                    user_input1 = int(input("Please enter your first number:\n"))   
                    user_input2 = int(input("Please enter your second number:\n"))   
                except ValueError:
                    print("Please enter only numbers.")  
                    break
                user_input_operator = input("Please enter one of the operators: +,-,*,/,% \n")
                equation = 0

                if user_input_operator == '+':
                    answer = user_input1 + user_input2
                elif user_input_operator == '-':
                    answer = user_input1 - user_input2
                elif user_input_operator == '*':
                    answer = user_input1 * user_input2
                elif user_input_operator == '/':
                    try:
                        answer = user_input1 / user_input2
                    except ZeroDivisionError :
                        print("Not possible to divide with zero. Enter some other number.")
                        break
                elif user_input_operator == '%':
                    try:
                        answer = user_input1 % user_input2
                    except ZeroDivisionError :
                        print("Not possible to divide with zero. Enter some other number.")
                        break
                else:
                    print("I am a simple calculator. I can perform only +,-,*,/ calculations. Please enter only one of these.")  
                    break
# Displaying the output on the console
                print("The equation is:")  
                equation = f"{user_input1} {user_input_operator} {user_input2} = {answer}"  
                print(equation)
# Appending the equations to the output file.A new file is created if it doesn't exist.
                f = open("Task 9_simple_calc.txt",'a')
                f.write("\n" + equation) 
                f.close()   
                break
            else:
                print("Wrong option entered.")          
                break
#Giving the user an option of running the program again or exit
        try:        
            run_program_again = int(input("Press 1 to continue , Any other key to exit: "))
            if run_program_again == 1:
                print("You opted to continue the program.")
            else:
                print("You opted to come out of the program.")  
                exit()
        except ValueError:
            exit()
            
          