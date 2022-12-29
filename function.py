from ping3 import ping
from urllib.parse import urlparse
from pickle import load
def test_speed(url:str):
    """测试访问速度
    website:被测网站"""
    pingtime=ping(urlparse(url).hostname)
    if pingtime !=None:
        return pingtime
    else:
        return float('inf')
def load_data(data_path:str):
    """读取数据文件
    data_path:数据文件路径"""
    with open(data_path,"rb") as data_file:
        data=load(data_file)
    return data
