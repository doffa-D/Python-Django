# Check the version of pip
pip3 --version

# Create a virtual environment named "local_lib"
python3 -m venv ./local_lib

# Activate the virtual environment
source ./local_lib/bin/activate

# Check if path.py is installed
pip freeze | grep path.py > /dev/null && echo "path.py is installed" || pip3 install git+https://github.com/jaraco/path.py.git >> logs.log 2>&1

# If path.py is installed, run my_program.py
if pip freeze | grep path.py > /dev/null; then
    python3 my_program.py
fi