import random
import argparse
import clipboard


def choice(string, num):
    random_str = [random.choice(string) for i in range(num)]
    return random_str


if __name__:
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')

    parser.add_argument(
        "-u",
        type=int,
        default=8,
        help='Number of Upper case Alphabet [default:8]')
    parser.add_argument(
        "-l",
        type=int,
        default=8,
        help='Number of Lower case Alphabet [default:8]')
    parser.add_argument(
        "-d",
        type=int,
        default=8,
        help='Number of Digits [default:8]')
    parser.add_argument(
        "-s",
        type=int,
        default=4,
        help='Number of Symbols (@ # $ %) [default:4]')

    args = parser.parse_args()

    string = "qwertyuiopasdfghjklzxcvbnm"
    digit = "0123456789"
    symbol = "@#$%"

    random_char = []
    for string_, num_ in zip(
            (string, string.upper(), digit, symbol), (args.l, args.u, args.d, args.s)):
        random_char += choice(string_, num_)
    random.shuffle(random_char)
    random_char = ''.join(random_char)
    print(random_char)
    clipboard.copy(random_char)
    print("copy to clipboard")
