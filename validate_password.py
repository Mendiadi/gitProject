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
        print(termcolor.colored("Password Not Strength!\n","red"), "\n".join(not_verify_list))
        exit(1)
    print(termcolor.colored("Password Strength!","green"))
    exit(0)


def from_file(args: list, args_count: int) -> None:
    """
    Read password from a given file.
    :param args: list of arguments
    :param args_count: len of list
    :return: None
    """
    if args_count == 2: # handle entering flag but nothing after
        print("expected file path after '-f' -> exit program")
        exit(1)
    elif args_count == 3: # handle file
        path = args[2]
        try:
            with open(path, "r") as f:
                password = f.read()
                verify_password(password)

        except FileNotFoundError:
            print("file not found -> exit program")
            exit(1)
    else: # handle too many arguments after -f
        print(f"invalid argument\n"
              f"expected one file path after '-f' but given "
              f"{args_count - 2} -> exit program")
        exit(1)


def main(args):
    colorama.init()  # init colorama module
    flag = "-f"
    args_count = len(args)
    """Handle Inputs"""
    if args_count <= 1: # handle no arguments situation
        print("invalid argument\n"
              "expected at least 1 argument -> exit program.")
        exit(1)
    if args[1] == flag:
        from_file(args, args_count)

    """Check the given password"""
    if args_count == 2: # handle password
        password = args[1]
        verify_password(password)

    else: # handle too many arguments situation
        print("invalid argument\n"
            f", expected 1 argument after space, but given {args_count - 1} -> exit program")
        exit(1)



if __name__ == '__main__':
    main(sys.argv)
