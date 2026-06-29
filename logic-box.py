while True:
    print("Welcome to the Pattern Generator and Number Analyzer")
    
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            while True:
                print("You like to generate the Pattern")
            
                print("Select any pattern from below:")
                print("1. Right Angle Triangle Pattern")
                print("2. Left Angle Triangle Pattern")
                print("3. Star pyramid Pattern")
                print("4. Exit")
            
                pattern_choice = input("Choose your Pattern: ")
                
                match pattern_choice:
                    case "1":
                        print("You have choosen right angle triangle pattern")
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                        
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(1, rows + 1):
                                    for j in range(i):
                                        print("*", end=" ")
                                    print()
                                    
                        else:
                            print("Rows value must be in Digit")
                            break
                        
                    case "2":
                        print("You have choosen left angle traingle pattern")
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                            
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(1, rows + 1):
                                    for j in range(i, rows):
                                        print(" ", end=" ")
                                    for k in range(i):
                                        print("*", end=" ")
                                    print()
                        else:
                            print("Rows value must be in Digit")
                            break
                    
                    case "3":
                        print("You have choosen star pyramid pattern")
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                            
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(0, rows):
                                    for j in range(i, rows-i-1):
                                        print(end=" ")
                                    for j in range(0, i + 1):
                                        print("*", end=" ")
                                    print()
                        else:
                            print("Rows value must be in digit")
                            break
                    case "4":
                        print("Exiting Pattern OPtion")
                        break
                        
                    case _:
                        print("Invalid INPUT")

        
        case "2":
            print("You would like to analyze the range of numbers")
            
            while True:
                print("Select any option from below:")
                print("1. Odd and Even numbers in the range")
                print("2. Sum of all numbers in the range")
                print("3. Exit")
                
                analyze_choice = input("Choose your option: ")
                
                match analyze_choice:
                    case "1":
                        print("You want Odd and Even numbers in the range")
                        
                        start_range = input("Enter the start of the range: ")
                        end_range = input("Enter the end of the range: ")
                        
                        if start_range.isdigit() and end_range.isdigit():
                            start_range = int(start_range)
                            end_range = int(end_range)
                            
                            if start_range >= end_range:
                                print("End range number value must be bigger than start range number")
                                break
                            else:
                                for i in range(start_range, end_range + 1):
                                    if i % 2 == 0:
                                        print(f"{i} is even number")
                                    else:
                                        print(f"{i} is odd number")
                        else:
                            print("Start range and End Raange must be in Digit")
                            break
                    
                    case "2":
                        print("You want sum of all numbers from start range to end range")
                        
                        start_range = input("Enter the start of the range: ")
                        end_range = input("Enter the end of the range: ")
                        
                        if start_range.isdigit() and end_range.isdigit():
                            start_range = int(start_range)
                            end_range = int(end_range)
                            
                            if start_range >= end_range:
                                print("End range number value must be bigger than start range number")
                                break
                            else:
                                sum = 0
                                for i in range(start_range, end_range + 1):
                                    sum += i
                                print(f"Sum of all numbers from {start_range} to {end_range} is: {sum}")
                        else:
                            print("Start range and end range must be in digit")
                        
                    case "3":
                        print("Thank you for Exploaring")
                        break
                    
                    case _:
                        print("Invalid Option")
                        break
        
        case "3":
            print("Exiting the Programme. Goodbye!!!")
            break
        
        case _:
            print("Invalid option")
            break
            