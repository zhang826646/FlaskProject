#
# def login_outer(fun):
#     def inner():
#         print("我是校验饰器")
#         fun()
#         print("给你校验后视图")
#     return inner
#
# def url_outer(fun):
#     def inner():
#         print("我是路由装饰器")
#         fun()
#         print("给你视图处理的结果")
#     return inner
#
# @url_outer
# @login_outer
# def views():
#     print("我是视图")
#
# views()

# import os
# os.system("ping 127.0.0.1")

# import datetime
# from models import Curriculum
# curr_list = ["php","java","c","c++","ui","html","linux","msyql","大数据"]
# for index,curr in enumerate(curr_list,2):
#     c = Curriculum()
#     c.c_id = "000%s"%index
#     c.c_name = curr
#     c.c_time = datetime.datetime.now()
#     c.save()






class Pager:
    """
    flask分页通过sqlalachemy查询进行分页
    offset 偏移，开始查询的位置
    limit 单页条数
    分页器需要具备的功能
    页码
    分页数据
    是否第一页
    是否最后一页
    """

    def __init__(self, data, page_size):
        """

        :param data: 要分页的数据
        :param page_size: 每页多少条
        """
        self.data = data #总数据
        self.page_size = page_size #单页数据
        self.is_start = False
        self.is_end = False
        self.page_count = len(data)

        self.page_nmuber = self.page_count/page_size
        #(data+page_size-1)//page_size
        if self.page_nmuber == int(self.page_nmuber):
            self.page_nmuber = int(self.page_nmuber)
        else:
            self.page_nmuber = int(self.page_nmuber)+1

        self.page_range = range(1,self.page_nmuber+1)#页码范围
    def page_data(self,page):
        """
        返回分页数据
        :param page: 页码
        page_size = 10
        1    offect 0  limit(10)
        2    offect 10 limit(10)
        page_size = 10
        1     start 0   end  10
        2     start 10   end  20
        3     start 20   end  30
        """
        if page <= self.page_range[-1]:
            page_start = (page - 1)*self.page_size
            page_end = page*self.page_size
            # data = self.data.offset(page_start).limit(self.page_size)
            data = self.data[page_start:page_end]
            if page == 1:
                self.is_start = True
            else:
                self.is_start = False
            if page == self.page_range[-1]:
                self.is_end = True
            else:
                self.is_end = False
        else:
            data = ["没有数据"]
        return data

# from models import Curriculum
# if __name__ == '__main__':
#     while True:
#         page = int(input("页码>>>"))
#
#         data = Curriculum.query.all()
#         page_size = 3
#         pager = Pager(data,page_size)
#         print("当前页码是：%s"%page)
#         print("共%s条数据" % (pager.page_count,))
#         print("总页数：%s"%(pager.page_nmuber,))
#         print("页码范围：%s"%str(list(pager.page_range)))
#         page_data = pager.page_data(page)
#         print("页面数据%s"%(page_data))
#         print("是否首页：%s"%(pager.is_start,))
#         print("是否尾页：%s"%(pager.is_end,))
#
#

# class Test:
#     name = 1
#     age = 2
#
# t = Test()
# print(t.name)
# print(t.age)
# setattr(t,"name",4)
# print(t.name)
# print(Test.name)

import requests

url = "http://sxpth.cn/"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
# }

req = requests.get(url)
response = req.content
print(response)