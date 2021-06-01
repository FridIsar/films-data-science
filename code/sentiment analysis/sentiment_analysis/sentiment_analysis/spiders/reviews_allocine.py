from scrapy import Request, Spider
from ..items import ReviewsAllocineItem


class SpiderReviewsAllocine(Spider):
    # Nom du spider
    name = "reviews_allocine"


    def start_requests(self):
        # URL de la page à scraper
        url = "https://www.allocine.fr/film/fichefilm-10568/critiques/spectateurs/"
        yield Request(url=url, callback=self.parse_films)

    def parse_films(self, response):
        title = response.css("a.titlebar-link::text").extract_first()
        review_blocks = response.css("div.review-card")
        for review_card in review_blocks:
            review = review_card.css("div.content-txt::text").extract_first()
            stars = review_card.css("span.stareval-note::text").extract_first()

            # Pour avoir la note (nombre d'étoiles) en float
            stars = float(stars.replace(",", "."))

            item = ReviewsAllocineItem()

            item['title'] = title
            item['stars'] = stars
            item['review'] = review

            yield item