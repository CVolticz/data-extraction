# Data Scraping Bot
A package used to establish a bot to scrape data on specified parameters predefined in configuration yaml file


## Installation
pip install git+https://github.com/burlingtonstores/scrapy.git@main


## How to Use
1. Declare configuration.yml file in the following way (with the dummy name of the place you want to scrape)
    - url: the web url
    - items: hash of items
        - sub-dictionary of items to scrape
            - each item in this dictionary should be an array of page extension and xpath in string format ["url-extension", "xpath"] 
```
TJMAX:
  url: https://tjmaxx.tjx.com/store/shop
  items:
    Women Dress: 
      Product Names: ['womens-dresses/_/N-3610029749?icid=5.10.22:TJMaxx:Homepage_Desktop::summer_shop_brands_hero_dresses', '//span[@data-rowclass="product-title"]/text()']
      Product Prices: ['womens-dresses/_/N-3610029749?icid=5.10.22:TJMaxx:Homepage_Desktop::summer_shop_brands_hero_dresses', '//span[@class="product-price"]/text()']
    Men Active Wear:
      Product Names: ['mens-activewear/_/N-696212721?ln=2:2', '//span[@data-rowclass="product-title"]/text()']
      Product Prices: ['mens-activewear/_/N-696212721?ln=2:2','//span[@class="product-price"]/text()']
```

2. Bot Initialization and Begin Scraping: Do whatever you want with the data ...
```
# Import the ConfigLoader and the Bot
from scrapy.Scrapy import Scrapy
from scrapy.utils.ConfigLoader import ConfigLoader

def get_data():
    # param initialization -> provide the path to your YML file in loadYaml
    params = ConfigLoader().loadYaml("../configs/web_page.yml")
    
    # Direct your url to whatever place you want to start
    # Can perform iteration here if you have multiple things... (write that yourself)
    url = params['TJMAX']['url']
    items = params['TJMAX']['items']

    # Steps to use the bot:
    # 1. initialize scraper bot -> point bot to a particular url
    # 2. load the items hash table onto the bot
    # 3. wait...
    # 4. Profit
    scraper_bot = Scrapy(url)
    data = scraper_bot.get_full_data(items)
    return data

# Don't be a coder, be a programer...
if __name__ == "__main__":
    data = get_data()
    print(data)
```


## Roadmap
Set up Github CI/CD
Add more functionality and further refinement on config yaml file. 

## Contributing
To contribute, create your own branch, develop, test and make a pull request to develop branch.

## Authors and acknowledgment
The Burlington Data Science Teams

## License
Burlington internal usage