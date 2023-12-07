import requests
import os

def get_url(message):
    return message.text

def like_video(url):
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.post("https://www.googleapis.com/youtube/v3/videos/like", headers=headers, params={"id": url})
    return response.status_code == 200

def take_screenshot(url):
    browser = webdriver.Chrome()
    browser.get(url)
    screenshot = browser.save_screenshot("screenshot.png")
    return screenshot

def share_screenshot(screenshot):
    with open("screenshot.png", "rb") as f:
        bot.send_photo(chat_id, f)

def main():
    message = bot.get_updates()[0]
    url = get_url(message)
    if like_video(url):
        screenshot = take_screenshot(url)
        share_screenshot(screenshot)

if __name__ == "__main__":
    main()
