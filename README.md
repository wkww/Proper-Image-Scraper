# Proper-Image-Scraper
###### Potentially useful if you're trying to build a CNN

Modern websites (2018) load images dynamically using javascript and frameworks such as React, Angular, Ember etc. Finding \<img> tags is not particularly helpful when the only static element loaded onto the DOM is \<div id='app'/>. 

Instead, we take advantage of the webdriver framework to download images as the browser loads them dynamically onto them DOM. You view the files that the browser is actually loading under the network section of your browsers developer console. By pulling images from the browser, we can even pull sprite sheets. 

Use your favorite webdriver Chrome, Firefox etc. or the recursive image scraper which is a Depth-First-Search(DFS) traversal of a site tree, so limit the depth wisely. 
