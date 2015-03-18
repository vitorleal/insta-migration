from migration import InstaMigration


def main():
    insta = InstaMigration('YOUR_INSTAGRAM_USER_NAME')
    insta.make_migration()


if __name__ == '__main__':
    main()
