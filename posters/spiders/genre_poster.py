# -*- coding: utf-8 -*-
import scrapy
from posters.items import Posters

class GenrePosterSpider(scrapy.Spider):
    name = "genre-posters-spider"
    urls = []
    genre = 'animation'
    start_urls = ['https://letterboxd.com/films/genre/' + genre + '/']

    def parse(self, response):
		# access to the data base
        database_url = response.css('#films-browser-list-container').xpath('@data-url')
        home = 'https://letterboxd.com'
        yield scrapy.Request(home + str(database_url.extract_first()), self.parse_page)

    def parse_page(self, response):
        # loop over all movies listed in the page just to the page and parse information
        img_url = response.css('ul li .react-component').css('img').xpath('@src').extract()
        data_id = response.css('ul li .react-component').xpath('@data-film-id').extract()
        for i in range(len(data_id)):
            img = img_url[i].split('?k=')[0]
            # create scrapy.items
            yield Posters(
                file_urls = [img])

        home = 'https://letterboxd.com'
        next_url = home + str(response.css('.paginate-next').xpath('@href').extract_first())
        page = int(response.css('.paginate-next').xpath('@href').extract_first().split('/page/')[1].split('/')[0])
        if page < 70:
            yield scrapy.Request(next_url, self.parse)
