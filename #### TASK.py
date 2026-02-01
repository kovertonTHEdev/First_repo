while True:
    line = input("Please, enter information: ").strip()
    if line == "help":
        print("Please, enter first info as the name of product, second info as the float number and third number as the int number" )
        continue
    elif line == "done":
        break
    parts = line.split()
    len(parts) != 3
    if len(parts) > 3:
        print ("Incorrect quantity")
