import tweepy
import requests
import time
import os

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
    url = "https://eager-meitner-f8adb8.netlify.app/.netlify/functions/random"
    response = requests.get(url)
    data = response.json()
    image_url = data['url']
    print(response.text)
    file_name = download_image(image_url)
    
    media = api.media_upload(file_name)
    id = api.update_status(status=f"{data['title']}\n\n{' '.join(data['twitter_hashtags'])}", media_ids=[media.media_id]).id

while True:
    try:
        run()
        break
    except Exception as e:
        print(e)
        time.sleep(5)
        pass