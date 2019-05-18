# -*- coding: UTF-8 -*-
fp = open("ximengyao.txt", encoding="utf-8", errors="ignore")
new_fp = open("ximengyao.txt.1", "w", encoding="gbk", errors="ignore")
try:
    all_text = fp.read()
    new_fp.write(all_text)
finally:
    fp.close()
    new_fp.close()
