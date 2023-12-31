import sys

def my_finder(state):
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

    if state in states:
        state_code = states[state]
        capital_city =  capital_cities[state_code]
        print(f"{capital_city}")
    else:
        print("Unknown state")
    


if __name__ == '__main__':
    if len(sys.argv) == 2:
        state = sys.argv[1].title()
        my_finder(state)
