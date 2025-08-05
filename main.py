from sealagom import navarea


# from db import connection
# import db

def main():
    for i in range(1, 20):
        if i != 13:
            navarea.collect_data()
    # db.connection.create()


if __name__ == '__main__':
    main()
