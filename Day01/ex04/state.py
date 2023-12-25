import sys

def my_finder(capital):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    for  state , capital_city in states.items():
        if capital_cities[capital_city] == capital:
            return(state)

    return "Unknown capital city"





if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(my_finder(sys.argv[1].title()))



