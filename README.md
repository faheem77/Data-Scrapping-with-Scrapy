# Data-Scrapping-with-Scrapy
Website scrapping with Scrapy

## Step by step instructions to run this spider


### Clone Repository
```
  git clone https://github.com/faheem77/Data-Scrapping-with-Scrapy.git
```
### Move  into the directory 
```
 cd Data-Scrapping-with-Scrapy
 ```
### Start virtual enviroment

```
    pipenv shell
```
### Install required library

``` 
   pip install -r requirements.txt
```

### Run Scrappy spider and save data in CSV file

```
    scrapy runspider scraper.py -O data.csv  
```
