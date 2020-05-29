import json

import scrapy

from spiderman.items import SpidermanItem


class DrugSpider(scrapy.Spider):
    name = 'drug'
    allowed_domains = ['code.nhsa.gov.cn']
    start_urls = ['http://code.nhsa.gov.cn:8000/yp/getPublishGoodsDataInfo.html?sysflag=95']

    page = 1
    data = {
        'companyNameSc': "",
        'registeredProductName': "",
        'approvalCode': "",
        'batchNumber': '20200507',
        '_search': "false",
        'nd': "1590664151676",
        'rows': '100',
        'page': str(page),
        'sidx': "t.goods_code",
        'sord': "asc"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=self.data, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/81.0.4044.138 Safari/537.36'})

    def parse(self, response):
        item = SpidermanItem()
        sites = json.loads(response.body_as_unicode())
        print(self, sites)
        rows = sites['rows']
        print(self, '当前第%d页，共%d条', self.page, len(rows))
        for row in rows:
            item['code'] = row['goodscode']
            item['name'] = row['registeredproductname']
            item['itemName'] = row['goodsname']
            item['dosageForm'] = row['registeredmedicinemodel']
            item['spec'] = row['registeredoutlook']
            item['packMaterial'] = row['materialname']
            item['minPack'] = row['factor']
            item['dosageUnit'] = row['unit']
            item['minPackUnit'] = row['minunit']
            item['company'] = row['companynamesc']
            item['num'] = row['approvalcode']
            item['standardCode'] = row['goodsstandardcode']
            if 'productinsurancetype' in row:
                item['classAB'] = row['productinsurancetype']
            else:
                item['classAB'] = ''
            if 'productcode' in row:
                item['serialNumber'] = row['productcode']
            else:
                item['serialNumber'] = ''
            if 'productname' in row:
                item['drugName'] = row['productname']
            else:
                item['drugName'] = ''
            if 'productmedicinemodel' in row:
                item['formulation'] = row['productmedicinemodel']
            else:
                item['formulation'] = ''
            item['remake'] = ''
            yield item
        if self.page < 880:
            self.page = self.page + 1
            self.data['page'] = str(self.page)
            yield scrapy.FormRequest(url=self.start_urls[0], formdata=self.data, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/81.0.4044.138 Safari/537.36'})
