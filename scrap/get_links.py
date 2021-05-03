import requests
import re
import webbrowser
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie
import urllib3
import time


def create_cookie_dict(rawdata='language=en; visid_incap_1095480=Lx3CtsEIRtqgXYl8UGNcb6d1fWAAAAAAQUIPAAAAAABHnxwGaIfTqXoqp7VCyUdJ; _ga=GA1.2.1643763137.1618834901; visid_incap_1882022=Qlrymk/+RS2NWtoaHb+QbNV1fWAAAAAAQUIPAAAAAADDtZGKfcyckqBApFcKYxnz; a=e95959f3fb8c4bb8adf705230829dda0; visid_incap_1637183=Asstp4IfQLeMvgbbwHvYPiB2fWAAAAAAQUIPAAAAAABg4YGU6LPCUjgeGlJ3hmNM; intercom-session-7knk2n3o=YTROV2FheDVpYjZRaUU5Q045eEVmL2YvYVhiSUs5RktVcUtscHRSQmtQaEJTdGNlZjBjYVRkQW1jSlhSazdweS0tcFdOUjZCQlIzWkYyR2JSTmlpZmJYUT09--9ee1196fdf82b8b62a6cd182…MCIsImxvZ2luSUQiOiJlOTU5NTlmM2ZiOGM0YmI4YWRmNzA1MjMwODI5ZGRhMCIsInVuaXF1ZV9uYW1lIjoiR2FsREByYS5yb2Nrd2VsbC5jb20iLCJzdWIiOiJHYWxEQHJhLnJvY2t3ZWxsLmNvbSIsImFtciI6InB3ZCIsImFjY0lkIjoiMjA0MjAxIiwiYXV0aFR5cGUiOiJVU0VSIiwiY2xvdWRpbmZyYS10ZW5hbnQtaWQiOiIiLCJjbG91ZGluZnJhLXRlbmFudC1yZWdpb24ta2V5IjoidXMiLCJjbG91ZGluZnJhLXVzZXItcm9sZSI6ImFkbWluIiwiY2xvdWRpbmZyYS11c2VyLWVtYWlsIjoiIiwiaXNzIjoiRG9tZTkiLCJhdWQiOiJ3ZWJhcHAiLCJleHAiOjE2MTkwOTQxNTAsIm5iZiI6MTYxOTA5MzU1MH0.PLNuVwoOcQNgCfHmVvshSOeuSUioepnj_nzQ-Oaaakc; _gat=1'):
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


proxies = {'https': 'http://127.0.0.1:8888'}
cookies = create_cookie_dict(rawdata='0c37852b34d0418e91c62ac25af4be5b161fc5b90a374129817860ad696762edi%3A0%23%2Ew%7Cd%5Fmaim%5Cportal2=0; 0c37852b34d0418e91c62ac25af4be5b161fc5b90a374129817860ad696762edi%3A0%23%2Ew%7Cd%5Fmaim%5Cportal1=0; SearchSession=771f8437%2D4274%2D489d%2Da5a7%2Dee7276222726; 0c37852b34d0418e91c62ac25af4be5b5abd7107da89435bbb454ade01c1717a=%3Ci%20p%3D%229fee55ef%2D70fd%2D48be%2Db58f%2De5121613585e%22%20m%3D%22RFcXWXU9rdpIbalryq95ddhWIXvtcy4faiypA2SdFnI%3D%22%20%2F%3E; databaseBtnText=0; databaseBtnDesc=0; stsSyncAppName=%D7%9C%D7%A7%D7%95%D7%97; stsSyncIconPath=; WSS_FullScreenMode=false')


def is_allowed_trace(url=""):
    resp = requests.options(url, verify=False, proxies=proxies, cookies=cookies)
    if 'TRACE' in resp.headers['Allow']:
        print(resp.headers)
        return True
    return False

trace_url_db = []
filepath = "water.txt"
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   try:
       while line:
           print("Line {}: {}".format(cnt, line.strip()))
           url = fp.readline().replace("\n", "")
           try:
               if is_allowed_trace(url):
                   trace_url_db.append(url)
                   time.sleep(1)
           finally:
               pass
           cnt += 1
   except:
       pass
   finally:
       pass

pass
