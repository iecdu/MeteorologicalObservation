import os
import requests
from urllib.parse import urlparse, unquote
# import xml.etree.ElementTree as xm
# from datetime import datetime
# import MySQLdb
import conn_mysql
from Weather_newVersion import MeteorologicalObservation

global m,d,h #设定全域变数，以月日时为檔名会用到

def download_xml(url, save_path):
    response = requests.get(url)

    if response.status_code == 200:
        # 使用urllib.parse解析URL获取文件名，并解码查询参数
        file_name = unquote(os.path.basename(urlparse(url).path)) # 解析的檔名为 00
        file_path = os.path.join(save_path,file_name) # 设成檔案路径
        # 檔案=os.path.join(路径,檔名)   str(m) +"_"+ str(d) +"_"+ str(h)

        MeteorologicalObservation(file_path) # 呼叫函式
        
        with open(file_path, 'wb') as file: # 保存文件
            file.write(response.content)
        print(f"XML文件已下载至: {file_path}")
        print()
    else:
        print(f"下载失败. HTTP状态码: {response.status_code}")
     
"""适用八月以后月份，需改进"""
# 自动替换url的月、日、时
d30 = range(16,31) # 
d31 = range(16,32)
for m in range(11,12):
    print(str(m)+"月")
    if  m%2 == 0:
        for d in d31:
            if len(str(d)) < 2:
                d = "0"+str(d)
                print(d,end=" ")
                print()
                for h in range(0,24):
                    if len(str(h)) < 2:
                        h = "0"+str(h)
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    else:
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    print(h,end=" ")
                    print(url)
                    # 指定URL和保存路径
                    xml_url = url
                    save_folder = r"C:\Users\User\Desktop\Weather\data"
                    # 调用函数进行下载
                    download_xml(xml_url, save_folder)
            else:
                print(d,end=" ")
                print()
                for h in range(0,24):
                    if len(str(h)) < 2:
                        h = "0"+str(h)                       
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    else:
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    print(h,end=" ")
                    print(url)
                    # 指定URL和保存路径
                    xml_url = url
                    save_folder = r"C:\Users\User\Desktop\Weather\data"
                    # 调用函数进行下载
                    download_xml(xml_url, save_folder)
    else:
        for d in d30:
            if len(str(d)) < 2:
                d = "0"+str(d)
                print(d,end=" ")
                print()
                for h in range(0,24):
                    if len(str(h)) < 2:
                        h = "0"+str(h)
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    else:
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    print(h,end=" ")
                    print(url)
                    # 指定URL和保存路径
                    xml_url = url
                    save_folder = r"C:\Users\User\Desktop\Weather\data"
                    # 调用函数进行下载
                    download_xml(xml_url, save_folder)
            else:
                print(d,end=" ")
                print()
                for h in range(0,24):
                    if len(str(h)) < 2:
                        h = "0"+str(h)
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    else:
                        url = "https://opendata.cwa.gov.tw/historyapi/v1/getData/O-A0001-001/2023/" + str(m) +"/"+ str(d) +"/"+ str(h) +"/00/00?Authorization=CWA-1731EFB9-BBD1-4AF4-9F13-E5534DACF038"
                    print(h,end=" ")
                    print(url)
                    # 指定URL和保存路径
                    xml_url = url
                    save_folder = r"C:\Users\User\Desktop\Weather\data"
                    # 调用函数进行下载
                    download_xml(xml_url, save_folder)

conn_mysql.dbsetting.close() # 关闭呼叫函数中使用的资料库连接
