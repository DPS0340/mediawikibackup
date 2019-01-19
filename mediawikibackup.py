#!/usr/bin/python3
import dropbox
import sys
import os
import pickle
from distutils.dir_util import copy_tree
import tarfile
from shutil import copyfile
from mysqlbackup import dbbackup

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == "__main__":
    backuppath, datetime = dbbackup.main()
    print("backup to dropbox...")
    with open(os.path.dirname(os.path.realpath(__file__)) + "/settings", "rb") as r:
        dict = pickle.load(r)
        secret = dict["SECRET"]
        WIKI_PATH = dict["WIKI_PATH"]
        nginx = dict["NGINX"]
        log = dict["LOG"]
    copy_tree(WIKI_PATH, backuppath + "/wiki")
    copyfile(nginx, backuppath + "/nginx")
    copyfile(log, backuppath + "/log")
    dbx = dropbox.Dropbox(secret)
    make_tarfile(os.path.dirname(os.path.realpath(__file__)) + "/backup/" + datetime+ ".tar", backuppath)
    with open(os.path.dirname(os.path.realpath(__file__)) + "/backup/" + datetime+ ".tar", "rb") as f:
        dbx.files_upload(f.read(), "/" + datetime + ".tar", mute=True)
    print("backup to dropbox complete!")
