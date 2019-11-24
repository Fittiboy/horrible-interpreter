print("Crython 3.7.4 (default, Jul  9 2019, 00:06:43)\n" +
    "[GCC 6.3.0 20170516] on linux")
while True:
    exec('code = """' + input(">>> ") + '"""')
    exec(code)