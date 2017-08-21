
import requests

class TestBook:
    def getbooks():
        url = 'https://jsonplaceholder.typicode.com/posts/1' 
        #params = {'year': year, 'author': author}
        #r = Request.get('http://api.example.com/books', params=params)
        r = requests.get(url)
        
        return r
        #books_list = {'books':books['results']}
      