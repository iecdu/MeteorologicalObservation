"""
    自動氣象站-氣象觀測
    短期過去資料解析
    2023-11-16 以后资料适用
"""
import xml.etree.ElementTree as xm
from datetime import datetime
import conn_mysql

def MeteorologicalObservation(data):

    data = xm.parse(data)        
    root = data.getroot() # 不需设立节点?
 
    for station in data.findall(".//{urn:cwa:gov:tw:cwacommon:0.1}Station"): #""" 路径.//看不懂 ，推测类似根目录"""
        StationName = station[0].text
        ObsTime = station.find("{urn:cwa:gov:tw:cwacommon:0.1}ObsTime")[0].text  
        ObsTime = datetime.fromisoformat(ObsTime).strftime("%Y-%m-%d %H:%M:%S") # 解析时间字段并转换为MySQL支持的格式
        # print(ObsTime)
        
        for GeoInfo in station.findall("{urn:cwa:gov:tw:cwacommon:0.1}GeoInfo"):
            """Coordinates"""
            CoordinateName_1 = GeoInfo[0][0].text
            Latitude_1 = GeoInfo[0][2].text
            Longitude_1 = GeoInfo[0][3].text
            CoordinateName_2 = GeoInfo[1][0].text
            Latitude_2 = GeoInfo[1][2].text
            Longitude_2 = GeoInfo[1][3].text
            Altitude = GeoInfo[2].text
            CountyName = GeoInfo[3].text
            TownName = GeoInfo[4].text
        for WeatherElement in station.findall("{urn:cwa:gov:tw:cwacommon:0.1}WeatherElement"):
            Weather = WeatherElement[0].text
            Precipitation = WeatherElement[1][0].text
            WE_WindDirection = WeatherElement[2].text 
            WindSpeed = WeatherElement[3].text
            WE_AirTemperature = WeatherElement[4].text
            RelativeHumidity = WeatherElement[5].text
            AirPressure = WeatherElement[6].text
        for GustInfo in WeatherElement.findall("{urn:cwa:gov:tw:cwacommon:0.1}GustInfo"):
            PeakGustSpeed = GustInfo[0].text
            Gust_WindDirection = GustInfo[1][0].text
            Gust_DateTime = GustInfo[1][1].text
            if Gust_DateTime[0] != "2":
                Gust_DateTime = "0000-00-00 00:00:00"
            else:
                Gust_DateTime = datetime.fromisoformat(Gust_DateTime).strftime("%Y-%m-%d %H:%M:%S")
        for DailyExtreme in WeatherElement.findall("{urn:cwa:gov:tw:cwacommon:0.1}DailyExtreme"):
            """DailyHigh"""
            DH_AirTemperature = DailyExtreme[0][0][0].text 
            DH_DateTime = DailyExtreme[0][0][1][0].text
            if DH_DateTime[0] != "2":
                DH_DateTime = "0000-00-00 00:00:00"
            else:
                DH_DateTime = datetime.fromisoformat(DH_DateTime).strftime("%Y-%m-%d %H:%M:%S")
            """DailyLow"""
            DL_AirTemperature = DailyExtreme[1][0][0].text # DailyLow
            DL_DateTime = DailyExtreme[1][0][1][0].text
            if DL_DateTime[0] != "2":
                DL_DateTime = "0000-00-00 00:00:00"
            else:
                DL_DateTime = datetime.fromisoformat(DL_DateTime).strftime("%Y-%m-%d %H:%M:%S")
          
            sql = "select ObsTime from MeteorologicalObservation where StationName='{}' and ObsTime='{}' and CountyName='{}' and TownName='{}'".format(StationName,ObsTime,CountyName,TownName)
            conn_mysql.cursor.execute(sql)        
            if conn_mysql.cursor.rowcount == 0:
                sql = "insert into MeteorologicalObservation(StationName,CoordinateName_1,Latitude_1,Longitude_1,\
                    CoordinateName_2,Latitude_2,Longitude_2,Altitude,CountyName,TownName,Weather,Precipitation,\
                    WE_WindDirection,WindSpeed,WE_AirTemperature,RelativeHumidity,AirPressure,PeakGustSpeed,\
                    Gust_WindDirection,Gust_DateTime,DH_AirTemperature,DH_DateTime,DL_AirTemperature,DL_DateTime,ObsTime) \
                    values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                    .format(StationName,CoordinateName_1,Latitude_1,Longitude_1,CoordinateName_2,Latitude_2,Longitude_2,
                            Altitude,CountyName,TownName,Weather,Precipitation,WE_WindDirection,WindSpeed,WE_AirTemperature,
                            RelativeHumidity,AirPressure,PeakGustSpeed,Gust_WindDirection,Gust_DateTime,
                            DH_AirTemperature,DH_DateTime,DL_AirTemperature,DL_DateTime,ObsTime)
                conn_mysql.cursor.execute(sql)
                conn_mysql.dbsetting.commit() 
                
                print(ObsTime)
                print(StationName)
                print(CoordinateName_1)
                print(Latitude_1,Longitude_1)
                print(CoordinateName_2)
                print(Latitude_2,Longitude_2)
                print(Altitude)
                print(CountyName,TownName,Weather)
                print(Precipitation)
                print(WE_WindDirection)
                print(WindSpeed)
                print(WE_AirTemperature)
                print(RelativeHumidity)
                print(AirPressure)
                print(PeakGustSpeed)
                print(Gust_WindDirection)
                print(Gust_DateTime)
                print(DH_AirTemperature)
                print(DH_DateTime)
                print(DL_AirTemperature)
                print(DL_DateTime)
                print()
# MeteorologicalObservation(r"C:\Users\User\Desktop\Weather\data\00") # 测试用
 
        #   另一种写法
        #     station_name = station.find("{urn:cwa:gov:tw:cwacommon:0.1}StationName").text
        #     station_id = station.find("{urn:cwa:gov:tw:cwacommon:0.1}StationId").text
        #     observation_time = station.find(".//{urn:cwa:gov:tw:cwacommon:0.1}DateTime").text
        #     print(f"气象站名称: {station_name}")
        #     print(f"气象站ID: {station_id}")
        #     print(f"观测时间: {observation_time}")
        # print(f"标签: {station.tag}, 文本内容: {station.text}")

"""
    xml.etree ElementTree简介
    https://blog.csdn.net/qq_43203949/article/details/108204223
    
"""
 
