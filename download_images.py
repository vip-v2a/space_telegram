import os
import requests
from urllib.parse import urlsplit, unquote
from dotenv import load_dotenv
from datetime import datetime


def download_image(url, dir, filename, params=None):
    response = requests.get(url, params)
    response.raise_for_status()

    filepath = f"{dir}/{filename}"

    with open(filepath, "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    """Find the latest launch fotos and download its."""

    spacex_dir = "images"
    spacex_url = "https://api.spacexdata.com/v4/launches"

    os.makedirs(spacex_dir, exist_ok=True)

    all_launches = requests.get(spacex_url)
    all_launches.raise_for_status()
    images_url = []

    for launch in all_launches.json()[::-1]:
        images_url = launch["links"]["flickr"]["original"]
        if images_url:
            break

    for index, image_url in enumerate(images_url):
        download_image(image_url, spacex_dir, f"spacex{index}.jpg")


def get_url_file_extension(url):
    url_path = urlsplit(url).path
    url_path = unquote(url_path)
    _, extension = os.path.splitext(url_path)
    return extension


def fetch_apod_pictures(api_key, count=10):
    """Download NASA Astronomy Picture of the Day (APOD).

    Args:
        api_key (str): NASA API Token.
        count (int, optional): Number of pictures to download.
            Defaults to 10.

    Returns:
        None.
    """
    apod_dir = "apod_images"
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"

    os.makedirs(apod_dir, exist_ok=True)

    params = {
        "api_key": api_key,
        "count": count
    }

    astronomy_pictures = requests.get(
        url=nasa_apod_url,
        params=params
    )
    astronomy_pictures.raise_for_status()

    for index, picture in enumerate(astronomy_pictures.json()):
        extension = get_url_file_extension(picture["url"])
        download_image(
            url=picture["url"],
            dir=apod_dir,
            filename=f"apod{index}{extension}"
        )


def fetch_epic_image(api_key, count=5):
    """Download NASA Earth Polychromatic Imaging Camera (EPIC).

    Args:
        api_key (str): NASA API Token.
        count (int, optional): Number of images to download.
            Defaults to 5.

    Returns:
        None.
    """
    epic_dir = "epic_images"
    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural/images"

    os.makedirs(epic_dir, exist_ok=True)

    params = {
        "api_key": api_key
    }

    epic_images = requests.get(nasa_epic_url, params)
    epic_images.raise_for_status()

    for index, image in enumerate(epic_images.json()):
        if index == count:
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
    nasa_epic_image_url = "https://api.nasa.gov/EPIC/archive/natural"
    date = datetime.strptime(date[:10], "%Y-%m-%d").date()
    date = f"{date:%Y/%m/%d}"
    url = f"{nasa_epic_image_url}/{date}/png/{name}.png"
    return url


def main():

    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")

    fetch_epic_image(nasa_api_key)

    fetch_apod_pictures(nasa_api_key)

    fetch_spacex_last_launch()

if __name__ == "__main__":
    main()
