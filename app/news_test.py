import unittest
from models import news 
News = news.News 

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'BBC News','Nine people arrested in china over Changsha building collapse','At least 18 people are trapped inside the largely-residential building which collapsed on Friday.','"https://www.aerotelegraph.com/millionen-bienen-sterben-auf-der-reise-mit-delta','https://ichef.bbci.co.uk/news/1024/branded_news/0D95/production/_124377430_gettyimages-1394602945.jpg','2022-05-01T11:22:23.3177183Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()