import re
#email

exp = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):

    if (re.search(exp, email)):
        print("Valid")
    else:
        print("Invalid")
if __name__ == '__main__':
    email = input("Enter your email : ")
    check(email)