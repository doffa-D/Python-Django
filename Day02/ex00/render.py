from settings import *
import sys
import os

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        contenu = ''.join(lines)
        a_ecrire = contenu.format_map(globals())
        file_html = file_path.replace('.template', '.html')
        with open(file_html, 'w') as file:
            file.write(a_ecrire)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: render.py <file.template>")
        exit(1)
    else:
        _, extension = os.path.splitext(sys.argv[1])
        if extension != ".template":
            print(f"Error: {extension} file should have .template extension")
            exit(1)
        main(sys.argv[1])

