
def podstring(str1, str2):
    # str1 = str1.upper()
    # str2 = str2.upper()
    # str1 = set(str1)
    # str2 = set(str2)
    str1 = set(letter.lower() for letter in str1 if letter.isalnum())
    str2 = set(letter.lower() for letter in str2 if letter.isalnum())

    if str2 <= str1:
        return True
    else:
        return False


if __name__ == '__main__':
    print('Unesi prvi string: ')
    s1 = input()
    print('Unesi drugi string: ')
    s2 = input()
    if podstring(s1, s2):
        print('Jeste')
    else:
        print('Nije')

    # print("S1: {1}\nS2: {0}".format(s2, s1))
    print(f"S1: {s1}\nS2: {s2}")
