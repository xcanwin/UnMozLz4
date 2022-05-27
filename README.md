# UnMozLz4

## 简介
- 一个用于解析火狐浏览器的jsonlz4与baklz4格式文件的Python库；
- 包括：previous.jsonlz4、recovery.jsonlz4、recovery.baklz4、upgrade.jsonlz4、bookmarks.jsonlz4、store.json.mozlz4等。

## 用法
```
from UnMozLz4 import UnMozLz4
mozLz4Bin = open('bookmarks-2010-01-01_2.jsonlz4', 'rb').read()
print(UnMozLz4(mozLz4Bin).unc())
```
