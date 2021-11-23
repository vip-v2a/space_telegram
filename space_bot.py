import os
from dotenv import load_dotenv
import time
import telegram


def main():

    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    delay = int(os.getenv("DELAY", default=86400))
    chat_id = os.getenv("CHAT_ID")

    image_folders = ["apod_images", "epic_images", "images"]

    bot = telegram.Bot(token=bot_token)

    while True:
        image_paths = get_image_paths(image_folders)
        for image_path in image_paths:
            post_image_in_telegram(image_path, bot, chat_id)
            time.sleep(delay)


def get_image_paths(image_folders):
    image_paths = []
    image_extensions = [".jpg", ".png"]
    for folder in image_folders:
        folder_images = os.listdir(folder)
        for image in folder_images:
            _, extension = os.path.splitext(image)
            if extension in image_extensions:
                image_paths.append(os.path.join(folder, image))
    return image_paths


def post_image_in_telegram(image_path, bot, chat_id):
    with open(image_path, "rb") as space_image:
        bot.send_photo(
            chat_id=chat_id,
            photo=space_image
        )


if __name__ == "__main__":
    main()
