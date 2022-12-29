from pickle import dump
image_dict={"阿里云镜像源":"http://mirrors.aliyun.com/pypi/simple/",\
            "中国科技大学镜像源":"https://pypi.mirrors.ustc.edu.cn/simple/",\
            "豆瓣镜像源":"http://pypi.douban.com/simple/",\
            "清华大学镜像源":"https://pypi.tuna.tsinghua.edu.cn/simple/"}
with open("image.data","wb") as data_file:
    dump(image_dict,data_file)
