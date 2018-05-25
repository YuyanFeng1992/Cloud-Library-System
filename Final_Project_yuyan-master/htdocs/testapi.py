import twitter


api = twitter.Api(consumer_key='6ettX3DHAbMKJKYTn8f2lfN97',consumer_secret='U8MdYGo09zEpyO75Po2z51uhekK3FSxH12frQrND7Km69tqnMl',access_token_key='891462251554770944-URUpURDfqNSq9eFU2p079fqdECrsNPN',access_token_secret='sA5qk6FmVyS8vk1VnfEWKRgfyJ8HGQGVkgYpIFLIvVAeY')
status = api.PostUpdate('We insert a new book!')