#!/usr/bin/env python3
#coding:utf-8
#instagram: instagram.com/neoax

###############################################################################

from scanners.htmli import htmlijection
from scanners.sqli import sqliscanner
from scanners.xss import xssscanner
from scanners.rfi import rfiscanner
from scanners.lfi import lfiscanner
from libs.crawler import crawler
from libs.banner import banner
from libs.check import check
import colorama
import argparse
import sys
import os

###############################################################################

k = "\033[91m"
y = "\033[92m"
s = "\033[93m"
b = "\033[0m"

###############################################################################

def main(url):
   check(url,veri.timeout,veri.method,agent)
   print(s+"[i]"+b+" Crawler başlatıldı.. ")
   links = crawler(url)
   print(s+"[i]"+b+" Güvenlik açığı tarama işlemi başlatıldı.. \n")
   for i in links:
       rfiscanner(i,veri.method,veri.timeout,agent)
       lfiscanner(i,veri.method,veri.timeout,agent)
       xssscanner(i,veri.method,veri.timeout,agent)
       htmlijection(i,veri.timeout,agent)
       sqliscanner(i,veri.method,veri.timeout,agent)
   print(s+"[i]"+b+" Tarama işlemi bitmiştir, iyi günler dilerim :) ")
   exit()
###############################################################################
agent = []
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help=u"Taranacak hedefi belirtmemize yarar.")
parser.add_argument("-U","--UserAgent", help=u"User agent eklemek için kullanılır.",default="Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51")
parser.add_argument("-r","--RandomAgent", help=u"Rastgele user agent kullan.",action="store_true")
parser.add_argument("-t","--timeout", help=u"Zaman aşımı süresi.",type=int,default=10)
parser.add_argument("-m","--method", help=u"Kullanılacak istek methodu [GET,POST]",default="GET")
veri = parser.parse_args()
agent.append(veri.UserAgent)
if veri.RandomAgent:
   ua = open("files/user-agent.vulnscan", "r").read().split()
   for a in ua:
      agent.append(a)
###############################################################################

if __name__=="__main__":
  banner()
  if veri.url:
     main(veri.url)
  else:
      os.system("python3 "+sys.argv[0]+" --help")
      
###############################################################################