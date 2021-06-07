# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsAllocineItem(scrapy.Item):
    
    title = scrapy.Field() # Le titre du film
    review = scrapy.Field() # Le commentaire
    stars = scrapy.Field() # La note donnée au film par l'auteur du commentaire
