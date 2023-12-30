# Import the sys module
import sys

# Add the path to the local library to the sys.path list
sys.path.insert(0, './local_lib/lib/python3.7/site-packages')

# Import the Path class from the path module
from path import Path

# Create a Path object representing the "./my_folder" directory
dir = Path("./my_folder")

# Create the "./my_folder" directory if it doesn't exist
dir.mkdir_p()

# Create a Path object representing the "./my_folder/my_file.txt" file
file = dir / "my_file.txt"

# Write the text "Hello World!\n" to the "./my_folder/my_file.txt" file
file.write_text("Hello World!\n")

# Read the contents of the "./my_folder/my_file.txt" file
content = file.read_text()

# Print the contents of the file
print(content)