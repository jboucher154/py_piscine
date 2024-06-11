import sys


def count_characters(string: str):
    """'count_characters'
    string: string to have characters counted from.
    The count of upper, lower, space, digit, and punctuation
    charcters in the string will be counted and printed out.
    """
    uppers = "".join(filter(lambda x: x.isupper(), string))
    lowers = "".join(filter(lambda x: x.islower(), string))
    spaces = "".join(filter(lambda x: x.isspace(), string))
    digits = "".join(filter(lambda x: x.isdigit(), string))
    char_count = len(uppers) + len(lowers) + len(spaces) + len(digits)
    punctuations = len(string) - char_count

    print(f"\nThe text contains {len(string)} characters:")
    print(f"{len(uppers)} upper letters")
    print(f"{len(lowers)} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{len(spaces)} spaces")
    print(f"{len(digits)} digits")


def main():
    """'main'
    This program take the first arg given or prompts
    the user for one. """
    try:
        argv = sys.argv
        argc = len(argv)
        assert argc <= 2, "more than one argument is provided"
        arg = ""
        if argc == 1:
            try:
                print("Please provide a string to be analyzed:")
                arg = sys.stdin.readline()
            except EOFError:
                pass
        else:
            arg = argv[1]

        count_characters(arg)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
