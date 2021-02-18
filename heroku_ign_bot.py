from os import environ

FORUM_COOKIE = environ['FORUM_COOKIE']


def main():
    print(FORUM_COOKIE)
    return FORUM_COOKIE


if __name__ == '__main__':
    main()
