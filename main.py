import region 
import age 
import date
import gender
import betweendates

def main():

    print('0. Quit\n'
        '1. Search by Date\n'
        '2. Search by Age\n'
        '3. Search by Region\n'
        '4. Search by Gender\n'
        '5. Search between dates\n')
    option = int(input("Option:\n "))

    
    while option != 0:
            
        if option == 1:
            date.searchbydate()
        elif option == 2:
            age.searchbyage()
        elif option == 3:
            region.searchbyregion()
        elif option == 4:
            gender.searchbygender()
        elif option == 5:
            betweendates.betweendate()

        while option < 0 or option > 5:
            print("Invalid option")
            main()
            
            #print('0. Quit\n'
            #'1. Search by Date\n'
            #'2. Search by Age\n'
            #'3. Search by Region\n'
            #'4. Search by Gender\n'
            #'5. Search between dates')

            #option = int(input("Option:\n "))
            

    
    
main()
