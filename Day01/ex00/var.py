def my_var():
    var = 42
    var1 = "42"
    var2 = "quarante-deux"
    var3 = 42.0
    var4 = True
    var5 = [42]
    var6 = {42: 42}
    var7 = (42,)
    var8 = set()
    print(f"{var} has a type {type(var)}")
    print(f"{var1} has a type {type(var1)}")
    print(f"{var2} has a type {type(var2)}")
    print(f"{var3} has a type {type(var3)}")
    print(f"{var4} has a type {type(var4)}")
    print(f"{var5} has a type {type(var5)}")
    print(f"{var6} has a type {type(var6)}")
    print(f"{var7} has a type {type(var7)}")
    print(f"{var8} has a type {type(var8)}")

if __name__ == '__main__':
    my_var()
