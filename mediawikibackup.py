import dropbox
import sys

if __name__ == "__main__":
    sys.path.insert(0, './python-mysql-backup')
    import dbbackup
    dbbackup.main()
    with open("secret", "r") as r:
        secret = r.readline()
    dbx = dropbox.Dropbox(secret)
    print(dbx.users_get_current_account())