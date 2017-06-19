# PosterSpider

PosterSpider is a Scrapy base web crawler for the movie profiles and movie posters

#### Run
To use, run
```
scrapy crawl [NAME OF SPIDER] -o [NAME OF OUTPUT FILE].json
```

###### List of Spiders
* *movie-rank* : Extracts the unique ids for the 250 movies from 2007 to 2016 and the index for the ranking by popularity
* *movie-spider* : Extracts the top 250 movies from 2007 to 2016
* *posters-spider* : Extracts the url for the poster images. For each image, get an unique id and title of the movie. Store the result in json format
* *genre-posters-spider* : Extracts the 5000 urls for the poster images of given genre of the movie
In order to change the output json file to jpg image file, run following command

```
cd output/full/
ls -l *.jpg | wc -l
```
