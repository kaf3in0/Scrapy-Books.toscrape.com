# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class BookCrawlerPipeline(object):
    def process_item(self, item, spider):
        # Navigate to the directory we want to save the images
        os.chdir('/home/edward/Desktop/images')

        # IF the image path exists
        if item['images'][0]['path']:
            # We rename the image to the book title
            new_image_name = item['title'][0] + '.jpg'
            new_image_path = 'full/' + new_image_name

            # Rename the file
            os.rename(item['images'][0]['path'], new_image_path)
