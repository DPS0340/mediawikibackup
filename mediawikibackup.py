import dropbox
if __name__ == "__main__":
    from python-mysql-backup import dbbackup
    with open("secret", "r") as r:
        secret = r.readline()
    dbx = dropbox.Dropbox(secret)
    print(dbx.users_get_current_account())