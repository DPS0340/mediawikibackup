import dropbox

with open("secret.txt", "r") as r:
    secret = r.readline()
dbx = dropbox.Dropbox(secret)
print(dbx.users_get_current_account())