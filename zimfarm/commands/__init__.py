import argparse

from . import login


def main():
    parser = argparse.ArgumentParser(description='Zimfarm Client')
    subparsers = parser.add_subparsers(dest="sub_parser", help='sub-commands')
    login.register(subparsers.add_parser('login'))
    args = parser.parse_args()

    sub_parser = args.sub_parser
    if sub_parser == 'login':
        login.process(args)


if __name__ == '__main__':
    main()


