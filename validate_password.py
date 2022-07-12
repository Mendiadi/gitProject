"""
    git project
"""
import termcolor
import colorama
import sys
import re

def verify_password(password: str) -> None:
    """
        Check the password regex and returns dict of result
        :param password: string
        :return: dict of msg and result
        """

    no_cap_msg = "Password must have at least one Capital letter"
    no_digits_msg = "Password must have at least one number"
    no_small_msg = "Password must have at least one small letter"
    len_under_10 = "Password length must be above 10"
    not_verify_list = []
    if not len(password) >= 10:
        not_verify_list.append(len_under_10)
    if not re.search("[a-z]", password):
        not_verify_list.append(no_small_msg)
    if not re.search("[0-9]", password):
        not_verify_list.append(no_digits_msg)
    if not re.search("[A-Z]", password):
        not_verify_list.append(no_cap_msg)
    if len(not_verify_list) > 0:
        print(termcolor.colored("Password Not Strength!\n", "red"), "\n".join(not_verify_list))
        exit(1)
    print(termcolor.colored("Password Strength!", "green"))
    exit(0)


def main(args):
    colorama.init()  # init colorama module
    args_count = len(args)
    """Handle Inputs"""
    if args_count <= 1:  # handle no arguments situation
        print("invalid argument\n"
              "expected at least 1 argument -> exit program.")
        exit(1)

    """Check the given password"""
    if args_count == 2:  # handle password
        password = args[1]
        verify_password(password)

    else:  # handle too many arguments situation
        print("invalid argument\n"
              f", expected 1 argument after space, but given {args_count - 1} -> exit program")
        exit(1)


if __name__ == '__main__':
    main(sys.argv)