num_1 = float(input("Enter number-1 ="))
num_2 = float(input("Enter number-2 ="))
choice = input("Enter your choice + - * / % =")

if choice == '+':
    print(f'add:{num_1 + num_2}')
    
elif choice == '-':
    print(f'sub:{num_1 - num_2}')
    
elif choice == '*':
    print(f'mul:{num_1 * num_2}')
elif choice == '/':
    
    print(f'div:{num_1 / num_2}')
    
elif choice == '%':
    print(f'modulas:{num_1 % num_2}')

else:
    print("un-valid choice")    
    