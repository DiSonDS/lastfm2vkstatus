import pylast
import vk_api
import time
import sys
from settings import *


def main():

    # Lastfm init
    network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=USERNAME,
        password_hash=pylast.md5(PASSWORD),
    )

    lastfm = network.get_user(USERNAME)

    # VK init
    vk_session = vk_api.VkApi(token=VK_USER_TOKEN)
    vk = vk_session.get_api()

    last_track = ""

    while True:
        if lastfm:
            results = lastfm.get_now_playing()
            if not results:
                if last_track:
                    last_track = ""
                    vk.status.set(text="")
                time.sleep(INTERVAL)
                continue
            if results != last_track:
                time_now = time.strftime("%H:%M", time.localtime())
                status_text = f"🎧 Last.fm | {results}"
                print(f"[{time_now}] {status_text}")
                vk.status.set(text=status_text)
                last_track = results
                time.sleep(INTERVAL)
            else:
                time.sleep(INTERVAL)
        else:
            print(f"Can't get user")
            sys.exit()


if __name__ == "__main__":
    main()
