# instagramfeed
Simple Instagram feed in HTML

![demo](https://github.com/bradster45/instagramfeed/blob/master/public/static/images/demo.JPG)

#### Key bits of code:

1) Context processor that is responsible for making the request to instagram, and creating the variables to pass to the template: [get_feed](https://github.com/bradster45/instagramfeed/blob/master/public/context_processors.py)



2) The HTML that uses the varaibles to construct the DOM: [div.instagram-feed-container](https://github.com/bradster45/instagramfeed/blob/master/public/templates/public/index.html)

3) [CSS](https://github.com/bradster45/instagramfeed/blob/master/public/static/css/instagram_feed.css)

