# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class SpidermanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 药品代码
    code = scrapy.Field()
    # 注册名称
    name = scrapy.Field()
    # 商品名称
    itemName = scrapy.Field()
    # 注册剂型
    dosageForm = scrapy.Field()
    # 注册规格
    spec = scrapy.Field()
    # 包装材质
    packMaterial = scrapy.Field()
    # 最小包装数量
    minPack = scrapy.Field()
    # 最小制剂单位
    dosageUnit = scrapy.Field()
    # 最小包装单位
    minPackUnit = scrapy.Field()
    # 药品企业
    company = scrapy.Field()
    # 批准文号
    num = scrapy.Field()
    # 药品本位码
    standardCode = scrapy.Field()

    # #####国家医保药品目录######
    # 甲乙类 productinsurancetype
    classAB = scrapy.Field()
    # 编号 productcode
    serialNumber = scrapy.Field()
    # 药品名称productname
    drugName = scrapy.Field()
    # 剂型productmedicinemodel
    formulation = scrapy.Field()
    # 备注
    remake = scrapy.Field()
    pass
