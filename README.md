# UnMozLz4
## 简介
```
用于解压火狐浏览器(Mozilla Firefox)的json文件(*.jsonlz4或者*.baklz4).
包括: previous.jsonlz4, recovery.jsonlz4, recovery.baklz4, upgrade.jsonlz4, bookmarks.jsonlz4, store.json.mozlz4
```

## 用法
```
from UnMozLz4 import UnMozLz4
mozLz4Bin = open('bookmarks-2010-01-01_2.jsonlz4', 'rb').read()
print(UnMozLz4(mozLz4Bin).unc())
```
