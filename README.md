# UnMozLz4
## 简介
```
用于解压火狐浏览器(Mozilla Firefox)的书签文件(*.jsonlz4), 为了方便调用, 我将解压方法封装为类.
```

## 用法
```
from UnMozLz4 import UnMozLz4
mozLz4Bin = file('bookmarks-2018-03-25_7.jsonlz4', 'rb').read()
print UnMozLz4(mozLz4Bin).unc()
```
