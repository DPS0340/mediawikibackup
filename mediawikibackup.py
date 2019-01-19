#!/usr/bin/python3
import google.cloud.storage
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
    storage_client = google.cloud.storage.Client()
    backuppath, datetime = dbbackup.main()
    print("backup to dropbox...")
    with open(os.path.dirname(os.path.realpath(__file__)) + "/settings", "rb") as r:
        dict = pickle.load(r)
        secret = dict["SECRET"]
        WIKI_PATH = dict["WIKI_PATH"]
        nginx = dict["NGINX"]
    copy_tree(WIKI_PATH, backuppath + "/wiki")
    copyfile(nginx, backuppath + "/nginx")
    bucket = storage_client.get_bucket(secret)
    blob = bucket.blob(os.path.basename(os.path.dirname(os.path.realpath(__file__)) + "/backup/" + datetime+ ".tar"))
    make_tarfile(os.path.dirname(os.path.realpath(__file__)) + "/backup/" + datetime+ ".tar", backuppath)
    blob.upload_from_filename(os.path.dirname(os.path.realpath(__file__)) + "/backup/" + datetime+ ".tar")
    print("backup to dropbox complete!")
