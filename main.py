from function import load_data,test_speed
from os.path import expanduser,abspath
from os import mkdir,listdir
from configparser import ConfigParser
from shutil import rmtree
from urllib.parse import urlparse
from sys import _MEIPASS
if __name__=="__main__":
    conf=ConfigParser()
    image_website=load_data("image.data")
    user_file=expanduser('~')
    keys_list=list(image_website.keys())
    visit_time=list()
    if "pip" in listdir(user_file):
        rmtree(user_file+"\\pip")
    mkdir(user_file+"\\pip")
    for i in keys_list:
        visit_time.append(test_speed(image_website[i]))
    winner_name=list(image_website.keys())[visit_time.index(min(visit_time))]
    winner_website=image_website[winner_name]
    print("最好的镜像源：{}（{}）\n正在写入文件".format(winner_name,winner_website))
    conf.add_section("global")
    conf.set("global","index-url",winner_website)
    conf.add_section("install")
    conf.set("install","trusted-host",urlparse(winner_website).hostname)
    with open(user_file+"\\pip\\pip.ini","w") as ini_file:
        conf.write(ini_file)
    input("写入文件成功，回车退出")
