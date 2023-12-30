# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import sys

# Create a class called roads_to_philosophy
class roads_to_philosophy():
    def __init__(self) -> None:
        self.prev = []  # Initialize an empty list to store visited titles
    
    def search_wikipeadia(self, path: str):
        URL = "https://en.wikipedia.org{}".format(path)  # Construct the URL using the provided path
        try:
            res = requests.get(URL)  # Send a GET request to the URL
            res.raise_for_status()  # Raise an exception if the response status is not 200
        except requests.HTTPError as e:
            if (res.status_code == 404):
                return print("It's a dead end !")  # If the page is not found, print a message
            return print(e)  # If any other HTTP error occurs, print the error message
        
        soup = BeautifulSoup(res.content, 'html.parser')  # Parse the HTML content using BeautifulSoup
        title = soup.find('span', {'class':'mw-page-title-main'})  # Find the main title of the page
        if title == None:
            print("Title not found")  # If the title is not found, print a message
            return
        
        title = title.text  # Get the text of the title
        link_element = soup.select_one("#mw-content-text .mw-parser-output p a")  # Find the first link in the content
        link = None
        if link_element is not None:
            link = link_element.get('href')  # Get the href attribute of the link
        
        if (title in self.prev):
            return print("It leads to an infinite loop !")  # If the title has already been visited, print a message
        
        self.prev.append(title)  # Add the title to the list of visited titles
        print(title)  # Print the current title
        
        if(title == "Philosophy"):
            return print("{} roads from {} to {} !".format(len(self.prev),self.prev[0],self.prev[len(self.prev) - 1]))
            # If the current title is "Philosophy", print the number of roads and the start and end titles
        
        self.search_wikipeadia(link)  # Recursively call the search_wikipeadia function with the next link

# Define the main function
def main():
    if len(sys.argv) != 2:
        print("Error to many arg")  # If the number of command line arguments is not 2, print an error message
        sys.exit(1)  # Exit the program with a non-zero status code

    wiki = roads_to_philosophy()  # Create an instance of the roads_to_philosophy class
    wiki.search_wikipeadia("/wiki/{}".format(sys.argv[1]))  # Call the search_wikipeadia method with the provided path

if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly
