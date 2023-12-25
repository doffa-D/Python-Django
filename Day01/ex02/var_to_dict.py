def store_dic(my_list):
    my_dict = {}
    for item in my_list:
        my_dict[item[1]] = item[0]
    return my_dict

def print_dict(my_dict):
    for key in my_dict:
        print(f"{key} : {my_dict[key]}")

if __name__ == '__main__':
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    my_d = store_dic(d)
    print_dict(my_d)