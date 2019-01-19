# mediawikibackup

dependency is only a python SDK of the dropbox APi v2.

```pip3 install dropbox```

git clone --recurse-submodules https://github.com/Shortwiki/mediawikibackup

```python3 setting.py``` to make setting file

then ```python3 mediawikibackup.py```

also, you can use crontab.

to use crontab, first type this:

```chmod a+x mediawikibackup.py```

set frequency and just write path of mediawikibackup.py in crontab.
