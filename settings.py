import pickle


if __name__ == "__main__":
    DB_HOST = input("please type DB_HOST.")
    DB_USER = input("please type DB_USER.")
    DB_USER_PASSWORD = input("please type DB_USER_PASSWORD.")
    DB_NAME = input("please type DB_NAME.")
    dump = {
        "DB_HOST":DB_HOST,
        "DB_USER":DB_USER,
        "DB_USER_PASSWORD":DB_USER_PASSWORD,
        "DB_NAME":DB_NAME
    }
    with open("./settings", "wb") as w:
        pickle.dump(dump, w)