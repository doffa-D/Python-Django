# Import necessary libraries
import requests  # For making HTTP requests
import sys  # For accessing command-line arguments
import dewiki  # For parsing Wikipedia text
import json  # For working with JSON data

# Define a function to retrieve Wikipedia content
def my_wikipedia(keyword):
    # Define the API endpoint URL
    url = "https://en.wikipedia.org/w/api.php"

    # Define the parameters for the API request
    param = {
        "action": "parse",
        "page": keyword,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        # Send a GET request to the API endpoint with the specified parameters
        res = requests.get(url, param)
        res.raise_for_status()  # Raise an exception if the request was unsuccessful
    except requests.HTTPError as e:
        print(f"Error: {e}")

    try:
        # Parse the response JSON data
        data = json.loads(res.text)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")

    # Return the parsed Wikipedia text
    return dewiki.from_string(data['parse']['wikitext']['*'])

# Entry point of the program
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Invalid number of command-line arguments")
        sys.exit(1)

    # Call the my_wikipedia function with the provided command-line argument
    wikitext = my_wikipedia(sys.argv[1])

    # Write the retrieved Wikipedia text to a file
    with open("{}.wiki".format(sys.argv[1]), 'w') as file:
        file.write(wikitext)
