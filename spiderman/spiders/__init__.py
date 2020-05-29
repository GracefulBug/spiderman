# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
if __name__ == '__main__':
    from scrapy import cmdline
    args = "scrapy crawl drug".split()
    cmdline.execute(args)