def parse_fun(line):
    elements = line.split("=")
    name = elements[0]
    pos , number , small, molar, electron = map(str.strip,elements[1].split(", "))
    pos = pos.split(":")[1].strip()
    number = number.split(":")[1].strip()
    small = small.split(":")[1].strip()
    molar = molar.split(":")[1].strip()
    electron = electron.split(":")[1].strip()
    Table = f"""
        <td style="border: 1px solid black; padding:10px">
            <h4>{name}</h4>
            <ul>
            <li>No {number}</li>
            <li>{small}</li>
            <li>{molar}</li>
            <li>{electron} electron</li>
            <ul>
        </td>

    """
    return Table


def fill_html(table):
    _Html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>DOFLAMINGO</title>
    <style>
        body {{
            font-family: "Futura PT", "Futura", "Helvetica", sans-serif;
            background-color: rgb(252, 244, 251);
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            color: rgb(0, 53, 99);
            text-align: center;
        }}
        li {{
            color: rgb(89, 79, 79);
            text-align: left;
        }}
        h4 {{
            text-align: center;
        }}

        table {{
            width: auto;
            border-collapse: collapse;
            margin: 20px;
        }}
        th,
        td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
            display: block; /* Display cells as blocks */
            width: 100%; /* Expand cells horizontally */
        }}

        th {{
            background-color: #007bff;
            color: white;
        }}

        td {{
            background-color: #fff;
        }}

        h4 {{
            margin-bottom: 10px;
            color: #007bff;
        }}

        ul {{
            list-style-type: none;
            padding: 0;
        }}

        li {{
            margin-bottom: 5px;
        }}
    </style>
</head>

<body>
    <h1>Periodic Table</h1>
    <table>
    <tr>
        {table}
    </tr>
    </table>
</body>
</html>
    """
    with open('periodic_table.html','w') as file:
        file.write(_Html)

def main(file_path):
    table = ""
    try:
        with open(file_path,'r') as file:
            for line in file:
                table += parse_fun(line.strip())
            fill_html(table)
    except FileNotFoundError:
        print(f"File {file_path} Not Found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    file_path = "periodic_table.txt"
    main(file_path)


