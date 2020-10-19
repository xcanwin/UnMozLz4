#!/usr/bin/env python3
# -- coding: utf-8 --
# author: xcanwin


class UnMozLz4():
    def __init__(self, mozLz4Bin):
        self.header = [109, 111, 122, 76, 122, 52, 48, 0]
        self.mozLz4List = [c for c in mozLz4Bin]

    def check(self):
        mozLz4List = self.mozLz4List
        header = self.header
        if mozLz4List[0:len(header)] == header:
            return True
        return False

    def getlz4len(self):
        mozLz4List = self.mozLz4List
        header = self.header
        headerLen = len(header)
        return (mozLz4List[headerLen]) \
             | (mozLz4List[headerLen + 1] << 8) \
             | (mozLz4List[headerLen + 2] << 16) \
             + (mozLz4List[headerLen + 3] * 0x1000000)

    def uncompresslz4(self):
        mozLz4List = self.mozLz4List
        lz4Length = self.lz4Length
        unLz4List = [0] * lz4Length
        mozLz4List = mozLz4List[len(self.header)+4:]
        i = 0
        j = 0
        while i < len(mozLz4List):
            token = mozLz4List[i]
            i += 1
            literals_length = token >> 4
            if literals_length > 0:
                l = literals_length + 240
                while l == 255:
                    l = mozLz4List[i]
                    i += 1
                    literals_length += l
                end = i + literals_length
                while i < end:
                    unLz4List[j] = mozLz4List[i]
                    j += 1
                    i += 1
                if i == len(mozLz4List):
                    return unLz4List
            offset = mozLz4List[i] | (mozLz4List[i+1] << 8)
            i += 2
            if offset == 0 or offset > j:
                return {}
            match_length = token & 0xf
            l = match_length + 240
            while l == 255:
                l = mozLz4List[i]
                i += 1
                match_length += l
            pos = j - offset
            end = j + match_length + 4
            while j < end:
                unLz4List[j] = unLz4List[pos]
                j += 1
                pos += 1
        return {}

    def unc(self):
        if self.check():
            self.lz4Length = self.getlz4len()
            if self.lz4Length > 0:
                unLz4List= self.uncompresslz4()
                unLz4Hex = ''.join([hex(d)[2:] for d in unLz4List])
                import binascii
                unLz4Bin = binascii.a2b_hex(unLz4Hex)
                return unLz4Bin
            else:
                print('[-] error: Content is null!')
                return None
        else:
            print('[-] error: This type of file is not supported!')
            return None


if __name__ == '__main__':
    # jsonlz4 or baklz4 file in C:\Users\xxx\AppData\Roaming\Mozilla\Firefox\Profiles\yyy.default\sessionstore-backups\ or .\bookmarkbackups\
    import sys
    if len(sys.argv) < 1:
        exit('python UnMozLz4.py bookmarks-demo.jsonlz4')
    else:
        readfile = sys.argv[1]
    from UnMozLz4 import UnMozLz4
    mozLz4Bin = open(readfile, 'rb').read()
    unLz4Bin = UnMozLz4(mozLz4Bin).unc()
    open('dec-' + readfile, 'wb').write(unLz4Bin)
    print('[+] Save: dec-' + readfile)

