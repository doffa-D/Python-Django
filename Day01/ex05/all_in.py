import sys

def fin_Captal(CP):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    for state ,capital_city in states.items():
        if CP == capital_city:
            return state
    return ""


def finder(find):
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

    for state , capital_city in states.items():
        if find == state:
            print(f"{capital_cities[capital_city]} is the capital of {state}")
            return 

    for capital_city , state in capital_cities.items():
        if find == state:
            print(f"{state} is the capital of {fin_Captal(capital_city)}")
            return 
    
    print(f"{find} is neither a capital city nor a state")
    return 



if __name__ == '__main__':
    for i in range(1,len(sys.argv)):
        for arg in sys.argv[1].split(', '):
            if arg.title().strip() != "":
                finder(arg.title().strip())
            