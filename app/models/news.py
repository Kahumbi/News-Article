class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,date,content):
        self.id =id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.date = date
        self.content = content