import openfoodfacts


def fetch_nutrition_score(item):

    try:
        search_result = openfoodfacts.products.search(item)
        grade = search_result['products'][0]['nutrition_grades']
        

    except:
        print('No grade found')

    else:
        return(grade)



