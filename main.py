from migration import InstaMigration
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', dest='username', type=str, required=True, help='Your Instagram user name')
    args = parser.parse_args()

    insta = InstaMigration(args.username)
    insta.make_migration()


if __name__ == '__main__':
    main()
