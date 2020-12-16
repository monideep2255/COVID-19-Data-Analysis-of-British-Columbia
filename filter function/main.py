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
        while ask != 'N':
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
        #earlier had an if statement which only asked the user once
        #for the the search
        #while loop helped solve the problem

        
    except:
        raise ValueError('The number must be between 0-5')
        raise TypeError('The number must be an integer')

    
              
main()
