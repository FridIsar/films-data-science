from re import search
from urllib.parse import urljoin
from scrapy import Request, Spider
from ..items import ReviewsAllocineItem

class SpiderReviewsAllocine(Spider):
    name = "reviews_allocine"
    domain = "http://www.allocine.fr/"
    
    # Le nombre de page limite (Nombre de films parcourues ~= 15*limit)
    limit = 3000

    # Nombre de commentaires par page
    reviews_per_page = 15

    # "entry_url" correspond à la section "Tous les films"
    entry_url = "http://www.allocine.fr/films/"

    # On a une erreur 403 quand on d'atteindre la page des commentaires sans un 'referer' et un 'user-agent' différent de celui de scrapy
    headers = {'referer': domain, 'user-agent':'Mozilla/5.0 (X11; Linux x86_64)'}

    def start_requests(self):
        for page in range(1, self.limit+1):
            url = urljoin(self.entry_url, f"?page={page}")

            yield Request(url=url, callback=self.parse_films, headers=self.headers)

    def parse_films(self, response):
        """
        Cette fontion parse la liste des film de la section 'Tous les films'
        Pour chacun des film de la section on va chercher le lien qui dirige sur la 
        page où se trouvent les commentaires des spectateurs : "http://www.allocine.fr/film/fichefilm-{id_film}/critiques/spectateurs/"
        l'identifiant du film se trouve dans le lien qui mene à la page 'détails' du film : '/film/fichefilm_gen_cfilm={id_film}.html'

        Args:
            response (Response): L'objet scrapy.Response qui correspond à la réponse de la requête faite dans 'start_requests'
        """
        # Liste des film de la page
        film_cards = response.css("main section.section ul > li.mdl > div.card")
        for film_card in film_cards: 
            title = film_card.css("div.meta > h2.meta-title a::text").extract_first()
            uri = film_card.css("div.meta > h2.meta-title a::attr(href)").extract_first()

            # On veut recupérer l'identifiant du film 268644 dans '/film/fichefilm_gen_cfilm=268644.html'
            id_film = search(r'/film/fichefilm_gen_cfilm=(.*?).html', uri).group(1)
            url_reviews = f"{self.domain}film/fichefilm-{id_film}/critiques/spectateurs/"

            yield Request(url=url_reviews, callback=self.parse_reviews, meta={'title': title, 'id_film': id_film, 'page': 1}, headers=self.headers)


    def parse_reviews(self, response):
        """
        Cette fonction parse les commentaires laissés par les spectateurs

        Args:
            response (Response): L'objet scrapy.Response qui correspond à la réponse de la requête faite dans 'start_requests'
        """
        review_cards = response.css("section.section div.review-card")
        for review_card in review_cards:
            review = review_card.css("div.content-txt::text").extract_first()
            review = review.strip()
            stars = review_card.css("span.stareval-note::text").extract_first()
            # Pour avoir la note (nombre d'étoiles) en float
            stars = float(stars.replace(",", "."))
            
            item = ReviewsAllocineItem()

            item['title'] = response.meta['title']
            item['stars'] = stars
            item['review'] = review

            yield item
        
        # Pagination
        if response.meta['page'] == 1:
            total_reviews = search(r'\d+', response.css("h2.titlebar-title::text").extract_first())
            total_reviews = int(total_reviews.group(0)) if total_reviews else 0
            
            # On lance une requete pour chacune des pages
            # +1 pour le reste et +1 parce que l'intervalle de range est ouvert à droite
            for page in range(2, int(total_reviews/self.reviews_per_page)+2):
                url = urljoin(response.url, f"?page={page}")
                response.meta['page'] = 2
                
                yield Request(url=url, callback=self.parse_reviews, meta=response.meta, headers=self.headers)
            


            
