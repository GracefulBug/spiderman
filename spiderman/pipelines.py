# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SpidermanPipeline(object):

    def __init__(self):
        self.db = pymysql.connect(host='123.56.142.9', user='root', passwd='pass', db='snh', charset='utf8',
                                  port=3306)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO lr_drug (code,name,item_name,dosage_form,spec,' \
              'pack_material,min_pack,dosage_unit,min_pack_unit,company,num,standard_code,' \
              'classAB,serial_number,drug_name,formulation,remake) ' \
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
        self.cur.execute(sql, (item['code'], item['name'], item['itemName'], item['dosageForm'], item['spec'],
                               item['packMaterial'], item['minPack'], item['dosageUnit'], item['minPackUnit'],
                               item['company'], item['num'], item['standardCode'], item['classAB'],
                               item['serialNumber'], item['drugName'], item['formulation'], item['remake']))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
