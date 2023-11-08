import os
import tweepy
import requests
import random

token = os.environ['TOKEN']
token_secret = os.environ['TOKEN_SECRET']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(token, token_secret)

api = tweepy.API(auth)

def download_image(url: str):
    content = requests.get(url).content
    # Check the extension of the image
    file_name = f"image.{url.split('.')[-1].split('?')[0]}"

    with open(file_name, 'wb') as file:
        file.write(content)

    return file_name


def run():
    url = "https://raw.githubusercontent.com/deep5050/programming-memes/main/memes.json"
    response = requests.get(url)
    data = random.choice(response.json())
    image_url = "https://raw.githubusercontent.com/deep5050/programming-memes/main/" + data['path']
    file_name = download_image(image_url)
    hashtags = ['#programming', '#Memes']    
    media = api.media_upload(file_name)
    id = api.create_tweet(text=f"{' '.join(hashtags)}", media_ids=[media.media_id])

run()
