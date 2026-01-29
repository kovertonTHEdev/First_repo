def format_string(string, length):
    spaces = (length - len(string)) // 2
    another_string = " " * spaces
    if len(string) >= length:
        return string
    if len(string) < length:
        return another_string + string     