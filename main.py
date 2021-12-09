def set_str():
    text = str(input("Задайте текст: "))
    return text


def set_list():
    s = set_str()
    a = list(s)
    return a


def check_for_char():
    check_for_this = ["@", "^", "#", "&"]
    checked_list = set_list()
    try:
        found_symvols = [x for x in checked_list + check_for_this if x not in checked_list]
        return found_symvols
    except:
        return check_for_this


print(check_for_char())
