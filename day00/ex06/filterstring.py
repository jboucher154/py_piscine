import sys
from ft_filter import ft_filter


def validate_args():
    """validate_args() --> str, int

Returns the string to process, int of length to filter by
from the commandline args passed. If incorrect args passed
assertion error is raised"""
    argv = sys.argv
    argc = len(argv)
    assert argc == 3, "the arguments are bad"
    string = argv[1]
    num = argv[2]
    try:
        num = int(num)
    except Exception:
        raise AssertionError("argument is not an integer")
    return string, num


def main():
    """main()

Prints list of words from passed string filtered by len of
integer passed.
    """
    try:
        S, N = validate_args()
        words = S.split()
        filtered_words = ft_filter(lambda word: len(word) > N, words)
        list_of_filtered = [word for word in filtered_words]
        print(list_of_filtered)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
