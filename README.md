# instagramfeed

Using Python requests, I generate a simple feed of Instagram posts by any non-private account. The feed has basic account stats and the last 12 posts. Images have hover effects to enlarge slightly. Posts are cached to avoid spamming Instagram.

Major pros of this approach is avoiding having to setup API keys or anything like that to authorise requests, and you can load a feed of any account without having to be logged in yourself. This is provided the account you wish to see a feed for is not set to private.

![demo](https://github.com/bradster45/instagramfeed/blob/master/public/static/images/demo.JPG)

#### Key bits of code:

1) Context processor that is responsible for making the request to instagram, and creating the variables to pass to the template: [get_feed](https://github.com/bradster45/instagramfeed/blob/master/public/context_processors.py)

2) The HTML that uses the varaibles to construct the DOM: [div.instagram-feed-container](https://github.com/bradster45/instagramfeed/blob/master/public/templates/public/index.html)

3) [CSS](https://github.com/bradster45/instagramfeed/blob/master/public/static/css/instagram_feed.css)

