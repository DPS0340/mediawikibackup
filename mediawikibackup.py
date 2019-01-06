import dropbox
import sys
import pickle
from distutils.dir_util import copy_tree


if __name__ == "__main__":
    sys.path.insert(0, './python-mysql-backup')
    import dbbackup
    backuppath = dbbackup.main()
    with open("secret", "r") as r:
        secret = r.readline()
    dbx = dropbox.Dropbox(secret)
    with open("./settings", "rb") as r:
        WIKI_PATH = pickle.load(r)["WIKI_PATH"]
    copy_tree(WIKI_PATH, backuppath + "wiki")
    print(dbx.users_get_current_account())