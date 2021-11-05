import os
import requests
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv
from datetime import datetime

SPACEX_URL = "https://api.spacexdata.com/v4/launches"
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_EPIC_IMAGE_URL = "https://api.nasa.gov/EPIC/archive/natural"
NASA_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural/images"


def download_image(url, dir, filename, params=None):
    response = requests.get(url, params)
    response.raise_for_status()

    filepath = f"{dir}/{filename}"

    with open(filepath, "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    
    """ Find lasest launch fotos and download its """

    spacex_dir = create_dir("images")

    all_launches = requests.get(SPACEX_URL)
    all_launches.raise_for_status()
    images_url_list = []

    for launche in all_launches.json()[::-1]:
        images_url_list = launche["links"]["flickr"]["original"]
        if images_url_list:
            break

    for index, image_url in enumerate(images_url_list):
        download_image(image_url, spacex_dir, f"spacex{index}.jpg")


def get_url_file_extension(url):
    url_path = urlsplit(url).path
    url_path = unquote(url_path)
    _, basename = os.path.split(url_path)
    _, extension = os.path.splitext(basename)
    return extension


def create_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir


def fetch_apod_pictures(api_key):
    
    """ Download NASA APOD (Astronomy Picture of the Day)"""

    apod_dir = create_dir("apod_images")

    params = {
        "api_key": api_key,
        "count": '10'
    }
    
    Astronomy_pictures = requests.get(
        url=NASA_APOD_URL,
        params=params
    )
    Astronomy_pictures.raise_for_status()

    for index, picture in enumerate(Astronomy_pictures.json()):
        picture_url = picture["url"]
        extension = get_url_file_extension(picture_url)
        download_image(
            url=picture_url,
            dir=apod_dir,
            filename=f"apod{index}{extension}"
        )


def fetch_epic_image(api_key):
    
    """ Download NASA EPIC (Earth Polychromatic Imaging Camera)"""

    image_count = 5
    epic_dir = create_dir("epic_images")

    params = {
        "api_key": api_key
    }

    epic_images = requests.get(NASA_EPIC_URL, params)
    epic_images.raise_for_status()

    for index, image in enumerate(epic_images.json()):
        if index == image_count:
            break
        image_url = get_epic_image_url(
            name=image["image"],
            date=image["date"])
        download_image(
            image_url,
            epic_dir,
            f"epic{index}.png",
            params            
        )


def get_epic_image_url(name, date):
    date = get_date_from_str(date)
    url = f"{NASA_EPIC_IMAGE_URL}/{date}/png/{name}.png"
    return url


def get_date_from_str(datestr):
    date = datetime.strptime(datestr[:10], "%Y-%m-%d").date()
    date = f"{date:%Y/%m/%d}"
    return date


def main():
    
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    
    fetch_epic_image(nasa_api_key)
    
    fetch_apod_pictures(nasa_api_key)

    fetch_spacex_last_launch()

if __name__=="__main__":
    main()