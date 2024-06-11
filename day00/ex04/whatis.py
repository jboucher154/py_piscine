import sys


argv = sys.argv
argc = len(argv)

if argc != 1:
    try:
        assert argc == 2, "more than one argument is provided"
        try:
            num = int(argv[1])
        except Exception:
            raise AssertionError("argument is not an integer")
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
