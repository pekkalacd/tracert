from urllib.parse import urlparse

class UrlMixin:

    def form_url(self):
        
        temp = self.url

        if 'http' not in temp:
            temp = 'http://' + temp
        elif 'www' not in temp:
            temp = 'www.' + temp

        return urlparse(temp)

    
    @classmethod
    def get_domain(cls, url):
        return url.replace("http://","").replace('www','')

    @classmethod
    def is_country(cls, ext):
        return ext not in {"com","org","net"}

    @classmethod
    def get_ext(cls, url):
        return url[-3:]



    
