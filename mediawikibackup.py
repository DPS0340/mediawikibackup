import dropbox

with open("secret.txt", "r") as r:
    secret = r.readline()
dbx = dropbox.dropbox(secret)
print(dbx.users_get_current_account())