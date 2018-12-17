import argparse

from . import login, logout


processors = {
    'login': login.process,
    'logout': logout.process
}


def main():
    parser = argparse.ArgumentParser(description='Zimfarm Client')
    subparsers = parser.add_subparsers(dest="sub_parser", help='sub-commands')

    login.register(subparsers.add_parser('login'))
    logout.register(subparsers.add_parser('logout'))

    args = parser.parse_args()

    sub_parser = args.sub_parser
    processor = processors.get(sub_parser)
    processor(args)


if __name__ == '__main__':
    main()


