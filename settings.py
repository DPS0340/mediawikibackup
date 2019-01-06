import pickle


if __name__ == "__main__":
    DB_HOST = input("please type DB_HOST.")
    DB_USER = input("please type DB_USER.")
    DB_USER_PASSWORD = input("please type DB_USER_PASSWORD.")
    DB_NAME = input("please type DB_NAME.")
    WIKI_PATH = input("please type WIKI_PATH.")
    dump = {
        "DB_HOST":DB_HOST,
        "DB_USER":DB_USER,
        "DB_USER_PASSWORD":DB_USER_PASSWORD,
        "DB_NAME":DB_NAME,
        "WIKI_PATH":WIKI_PATH
    }
    with open("./settings", "wb") as w:
        pickle.dump(dump, w)