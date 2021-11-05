import os
from dotenv import load_dotenv
import time
import telegram


def main():

    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    delay = int(os.getenv("DELAY", default=60*60*24))
    chat_id = "@myspacephotos"

    images_paths = iter(get_images_paths())
    while True:
        bot = telegram.Bot(token=bot_token)
        bot.send_photo(
            chat_id=chat_id,
            photo=open(next(images_paths), "rb")
        )
        time.sleep(delay)


def get_images_paths():
    images_paths = []
    image_extensions = [".jpg", ".png"]
    files = os.listdir(".")
    images_folders = filter(lambda x: "image" in x, files)
    for folder in images_folders:
        folder_images = os.listdir(folder)
        for image in folder_images:
            _, extension = os.path.splitext(image)
            if extension in image_extensions:
                images_paths.append(os.path.join(folder, image))
    return images_paths


if __name__ == "__main__":
    main()
