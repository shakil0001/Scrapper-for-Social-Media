from src.InstagramScrapper import InstagramScrapper
from src.TwitterScrapper import TwitterScrapper

if __name__ == '__main__':

    print("Starting Scrapper for Social Media...")
    keyword = str(input("Enter keyword to search for: "))
    insta_limit = int(input("Enter how many posts to scrape from Instagram: "))
    twitter_limit = int(input("Enter how many posts to scrape from Twitter: "))

    consumerKey = '5FkDTUvwhsacdcasxa3faQ8PDZjoFgk'
    consumerSecret = 'ArGbXU4csFAqfjsoNCjBvCHxUngTiXx8q4oZNtZa8'
    accessToken = '104298691515729510xxzccndIbl53V6x2AUl3JOhWt5Cp'
    accessTokenSecret = 'wGAYDiYNKjD5ssxsJWPMFueyIkSpBNWGq2KVn06'


    scrapper = InstagramScrapper()
    scrapper.Scrape_Instagram(tag=keyword,
                              limit=insta_limit,
                              browser='firefox') # 'chrome' or 'firefox'


    twitter = TwitterScrapper()
    twitter.Scrape_Twitter(Consumer_Key=consumerKey,
                           Consumer_Secret=consumerSecret,
                           Access_Token=accessToken,
                           Access_Token_Secret=accessTokenSecret,
                           tag=keyword,
                           limit=twitter_limit,
                           lang='en')  # Language codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


    print("Stopping Scrapper for Social Media...")
