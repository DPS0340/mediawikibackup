# mediawikibackup

dependency is only a google cloud storage api.

```pip install google-cloud-storage```

git clone --recurse-submodules https://github.com/DPS0340/mediawikibackup

run setting.py to make setting file

then run mediawikibackup.py

also, you can use crontab.

to use crontab, first type this:

```chmod a+x mediawikibackup.py```

set frequency and just write path of mediawikibackup.py in crontab.
