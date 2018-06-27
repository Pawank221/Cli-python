import urllib
import requests
import cv2
url = "https://api.pexels.com/v1/curated?per_page=15&page=1"
headers = {
    'Authorization': 'key missing'
}

def do_wallpaper():

    response = requests.get(url, headers=headers).json()
    photos_url = [obj['src']['original'] for obj in response['photos']]
    for link in photos_url:
        print(link)
        cv2.namedWindow("Image")
        cv2.imshow("Image",link)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
