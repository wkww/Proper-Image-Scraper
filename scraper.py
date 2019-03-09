from selenium import webdriver
import wget
import os 

base_dir = os.path.dirname(os.path.abspath(__file__))
prefix= 'images'
path = os.path.join(base_dir, prefix)
if not os.path.exists(path):
    os.mkdir(path)
if not os.path.isdir(path):
    exit()


def getNetworkImages(driver):
    ImageList = []
    Resources = driver.execute_script("return window.performance.getEntriesByType('resource');")

    for resource in Resources:
        if resource['name'].endswith(('.jpeg','jpg','.tiff','.gif','.png','.bmp','.svg')): 
            ImageList.append(resource['name'])
    for url in ImageList:
        print('Beginning file download with wget module') 
        
        wget.download(url, out=path) 
    return ImageList


#Replace with your URL insert combine this module with a domain scraper 
url = "https://www.google.com/"

# loads page and downloads files with image extensions
def loadPage(url):
    
    #replace with .Firefox(), or with the webdriver of your choice
    browser = webdriver.Chrome()
    browser.get(url)
    imagelist = getNetworkImages(browser)

if __name__ == "__main__":
    loadPage(url)
