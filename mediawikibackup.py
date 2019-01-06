import dropbox
import sys
import os
import pickle
from distutils.dir_util import copy_tree
import tarfile

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == "__main__":
    sys.path.insert(0, './python-mysql-backup')
    import dbbackup
    backuppath, datetime = dbbackup.main()
    with open("secret", "r") as r:
        secret = r.readline()
    with open("./settings", "rb") as r:
        WIKI_PATH = pickle.load(r)["WIKI_PATH"]
    copy_tree(WIKI_PATH, backuppath + "/wiki")
    dbx = dropbox.Dropbox(secret)
    make_tarfile("./backup/" + datetime+ ".tar", backuppath)
    with open("./backup/" + datetime+ ".tar", "rb") as f:
        dbx.files_upload(f.read(), "/" + datetime + ".tar", mute=True)
    print("backup to dropbox complete!")