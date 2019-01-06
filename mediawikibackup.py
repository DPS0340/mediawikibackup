import dropbox
import sys
import os
import pickle
from distutils.dir_util import copy_tree
import tarfile
from shutil import copyfile

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == "__main__":
    from mysqlbackup import dbbackup
    backuppath, datetime = dbbackup.main()
    with open("./settings", "rb") as r:
        dict = pickle.load(r)
        secret = dict["SECRET"]
        WIKI_PATH = dict["WIKI_PATH"]
        nginx = dict["NGINX"]
    copy_tree(WIKI_PATH, backuppath + "/wiki")
    copyfile(nginx, backuppath + "/nginx")
    dbx = dropbox.Dropbox(secret)
    make_tarfile("./backup/" + datetime+ ".tar", backuppath)
    with open("./backup/" + datetime+ ".tar", "rb") as f:
        dbx.files_upload(f.read(), "/" + datetime + ".tar", mute=True)
    print("backup to dropbox complete!")