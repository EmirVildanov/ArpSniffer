def print_red(text):
    WARNING = '\033[91m'
    ENDC = '\033[0m'
    print(f"{WARNING}{text}{ENDC}")


def print_green(text):
    GOOD = '\033[92m'
    ENDC = '\033[0m'
    print(f"{GOOD}{text}{ENDC}")