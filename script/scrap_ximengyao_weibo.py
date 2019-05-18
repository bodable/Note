# -*- coding: UTF-8 -*- 
import requests
import json
import io
import re
import traceback

# source_wei_wo_url = "https://m.weibo.cn/status/4176281144304232"


def get_comment(head_url, count):
    i = 1
    fp = io.open("ximengyao.txt", "a", encoding="utf8")
    while i <= count:
        print(i)
        i += 1
        try:
            url = head_url + str(i)
            resp = requests.get(url)
            resp.encoding = resp.apparent_encoding
            try:
                comment_json = json.loads(resp.text)
                print(comment_json)
                comments_list = comment_json["data"]["data"]
                print(comments_list)
            except Exception as e:
                print(e)
                continue
            commment_num = 0
            for commment_item in comments_list:
                commment_num += 1
                username = commment_item["user"]["screen_name"]
                comment = commment_item["text"]
                label_filter = re.compile(r'</?\w+[^>]*>', re.S)
                comment = re.sub(label_filter, '', comment)
                fp.write(comment)
                if commment_num > 10:
                    break
            #print(i)
        except Exception as e:
            traceback.print_exc()
            continue
    fp.close()


if __name__ == "__main__":
    head_url = "https://m.weibo.cn/api/comments/show?id=4176281144304232&page="
    get_comment(head_url, 1)
