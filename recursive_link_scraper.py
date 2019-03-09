from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://www.google.com"

# Merges dictionaries but keeps larger key values
def merge_dicts(dict1, dict2):
    merged = dict(dict1)
    for key in dict2:
        if key not in merged or dict2[key] > merged[key]:
            merged[key] = dict2[key]
    return merged

def getUrls(url, xpath_query):
	driver.get(url)
	elems = driver.find_elements_by_xpath("//a[@href]")
	url_list = [i.get_attribute("href") for i in elems]
	url_dict = {i:0 for i in url_list}
	return url_dict

def getUrlsRecursive(url,url_dict, xpath_query, depth=1):
	if(depth>0):
		driver.get(url)
		elems = driver.find_elements_by_xpath("//a[@href]")
		url_list = [i.get_attribute("href") for i in elems]
		url_dict2 = {i:0 for i in url_list}
		url_dict = merge_dicts(url_dict, url_dict2)

		if url in url_dict:
			url_dict[url] = url_dict[url]+1

		for item in url_dict:

			print('***********')
			print(url_dict[item])
			if url_dict[item]==0:
				urls = getUrlsRecursive(item, url_dict, xpath_query,depth-1)
				#list merging --order determines which value is kept in the case of identical keys
				url_dict = merge_dicts(urls, url_dict)
			else:
				url_dict[item]=url_dict[item]+1
		return url_dict
	else:
		return {}

print(getUrlsRecursive(url,{}, "//a[@href]", 2))



