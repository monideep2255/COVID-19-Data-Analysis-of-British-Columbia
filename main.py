import region 
import age 
import date
import gender

def main():

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
        else:
            exit

        
    except:
        raise ValueError('The number must be between 0-5')
        raise TypeError('The number must be an integer')

    
    #comment that while was not used since it was creating a loop
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
