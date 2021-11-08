import os
from dotenv import load_dotenv
import time
import telegram


def main():

    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    delay = int(os.getenv("DELAY", default=60*60*24))
    chat_id = os.getenv("CHAT_ID")
    
    images_folders = ["apod_images", "epic_images", "images"]
    
    bot = telegram.Bot(token=bot_token)

    while True:
        images_paths = get_images_paths(images_folders)
        for image_path in images_paths:
            with open(image_path, "rb") as space_image:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=space_image
                )
            time.sleep(delay)


def get_images_paths(images_folders):
    images_paths = []
    image_extensions = [".jpg", ".png"]
    for folder in images_folders:
        folder_images = os.listdir(folder)
        for image in folder_images:
            _, extension = os.path.splitext(image)
            if extension in image_extensions:
                images_paths.append(os.path.join(folder, image))
    return images_paths


if __name__ == "__main__":
    main()
