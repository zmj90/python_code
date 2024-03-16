"""
    业务逻辑层
"""
from dal import HouseDao


class HouseManagerController:
    """
        房源信息管理系统控制器：负责处理业务逻辑
    """

    def __init__(self):
        """
            创建房源信息管理系统控制器
        """
        self.list_houses = HouseDao.load()

    def get_house_by_max_total_price(self):
        # 写法1：简单但不灵活
        # 重写模型的__gt__方法
        # return max(self.__list_houses)
        # 写法2： 内置高阶函数(性能高)
        return max(self.list_houses,key = lambda house:house.total_price)

    def get_house_by_min_area(self):
        return min(self.list_houses, key=lambda item: item.area)

    def ascending_by_total_price(self):
        return sorted(self.list_houses, key=lambda element: element.total_price)
