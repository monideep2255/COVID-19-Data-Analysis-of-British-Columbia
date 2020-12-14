import region #main page of the filter function
import age 
import date
import gender

#made the decision to make this program modular since:
#modularity makes the program more efficient and easy to understand
#easy for debugging and modifying purposes

def main():
    #function: main
    #parameters: none
    #return: home page to filter the dataset based on different options

    try:
        print('0. Quit\n'
            '1. Search by Date\n'
            '2. Search by Age\n'
            '3. Search by Region\n'
            '4. Search by Gender\n')

        option = int(input("Option:\n "))

        if option == 1:
            date.searchbydate()
        elif option == 2:
            age.searchbyage()
        elif option == 3:
            region.searchbyregion()
        elif option == 4:
            gender.searchbygender()

        ask = input('Do you want to perform any more searches (Y/N)?')
        if ask == 'Y':
            print('0. Quit\n'
            '1. Search by Date\n'
            '2. Search by Age\n'
            '3. Search by Region\n'
            '4. Search by Gender\n')

            option = int(input("Option:\n "))

            if option == 1:
                date.searchbydate()
            elif option == 2:
                age.searchbyage()
            elif option == 3:
                region.searchbyregion()
            elif option == 4:
                gender.searchbygender()
        else:
            exit

        
    except:
        raise ValueError('The number must be between 0-5')
        raise TypeError('The number must be an integer')

    
#initally had plans to use the while loop but had trouble getting out of the loop
    #while option < 0 or option > 5:
        #print("Invalid option")
            
            
        #print('0. Quit\n'
            #'1. Search by Date\n'
            #'2. Search by Age\n'
            #'3. Search by Region\n'
            #'4. Search by Gender\n'
            #'5. Search between dates')
        #option = int(input("Option:\n "))
              
main()
