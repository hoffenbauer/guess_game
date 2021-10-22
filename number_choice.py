if __name__ == '__main__':
    main()

def number_validation(bottom = 0, top = 10):
    choice = ""
    
    while choice.isdigit() == False or int(choice) not in range(bottom, top):
        
        choice = input(f"Please, insert a number from {bottom} to {top}: ")
        
        if choice.isdigit() == False:
            choice = input(f"Please, insert a valid number from {bottom} to {top}: ")
            
    return int(choice)