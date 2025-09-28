print("Welcome to the data Analyzer and Transformer Program")
data_list=[]
while True:
    print("Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary(Built in Function)")
    print("3.Calculate Factorial(recursion)")
    print("4.Filter Data by Threshold(Lambda Function)")
    print("5.Sort data")
    print("6.Display Data Statistics(Return multiple values)")
    print("7.Exit Program")
    
    choice=int(input("Please Enter your Choice:"))

    match choice:
        case 1:
            data_list
            try:
                data_srt = input("Enter data (numbers separated by spaces):")
                data_list = [int(x) for x in data_srt.split()]
                print("Data stored successfully!")
            except ValueError:
                print("Error: Please enter valid numbers.")
        case 2:
            if not data_list:
                print("Please add data elements:")
            else:
                
                print("Data Summary:")
                print("Total Element:",len(data_list))
                print("Minimum Value:",min(data_list))
                print("Maximum value:",max(data_list))
                print("Sum of all values:",sum(data_list))
        case 3:
            n=int(input("Enter a number to calculate its Factorial:"))
            def fact(n):
                if n<2:
                    return 1
                else:
                    return n*fact(n-1)
            ans=fact(n)
            print(ans)
        case 4:
            if not data_list:
                print("List is empty ,please insert list first!")
            else:
                i=int(input("Enter a threshold value to filter out data above this value:"))
                filtered_list = list(filter(lambda x: x >= i, data_list))
                print(f"Filtered Data (values >= {i}): {filtered_list}")
        case 5:
            print("choose your Option:")
            print("1.Ascending")
            print("2.Descending")

            option=int(input("Enter your Choise:"))
            if option==1:
                sorted_data=sorted(data_list)
                print("Sorted data in Ascending Order:")
                print(sorted_data)
            elif option==2:
                print("Sorted data in Descending")
                data_list.sort(reverse=True)
                print(data_list)
            else:
                print("Invalid Choise")
        case 6:
            if not data_list:
                print("None")
            else:
                minimum = min(data_list)
                maximum = max(data_list)
                total_sum = sum(data_list)
                average = total_sum / len(data_list)
                print(f"Minimum value:",minimum)
                print(f"Maximum value:",maximum)
                print(f"Sum of values:",total_sum)
                print(f"Average value:",average)
        case 7:
            print("\n Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
            print("Invalid Choice. Try again!")
                











                

