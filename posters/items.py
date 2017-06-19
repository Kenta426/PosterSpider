# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
Collect the posters along with the information
'''
class PostersItem(scrapy.Item):
    ''' Item for the movie posters '''
    data_id = scrapy.Field() # unique id for each poster
    title = scrapy.Field() # title of the movie
    file_urls = scrapy.Field() # url for the images
    files = scrapy.Field() # actual image

'''
Collect the profile of the movie
'''
class MovieData(scrapy.Item):
    # data about the movie itself
    data_id = scrapy.Field() # unique id for each movie
    title = scrapy.Field() # title of the movie
    year = scrapy.Field() # year released
    genre = scrapy.Field() # genre of the movie
    imdb_id = scrapy.Field() # imdb score

'''
Get ranking for the movie item
'''
class MovieRankByPopularity(scrapy.Item):
    # data about the movie itself
    data_id = scrapy.Field() # unique id for each movie
    rank = scrapy.Field() # rank of the movie by letterboxd


'''
Only collect the image
'''
class Posters(scrapy.Item):
    file_urls = scrapy.Field() # url for the images
    files = scrapy.Field() # actual image
