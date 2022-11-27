import sys
import time

import pylast
import vk_api

import settings


def main():

    # Lastfm init
    network = pylast.LastFMNetwork(
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
        username=settings.USERNAME,
        password_hash=pylast.md5(settings.PASSWORD),
    )

    lastfm = network.get_user(settings.USERNAME)

    # VK init
    vk_session = vk_api.VkApi(token=settings.VK_USER_TOKEN)
    vk = vk_session.get_api()

    last_track = ""

    while True:
        if lastfm:
            results = lastfm.get_now_playing()
            if not results:
                if last_track:
                    last_track = ""
                    vk.status.set(text="")
                time.sleep(settings.INTERVAL)
                continue
            if results != last_track:
                time_now = time.strftime("%H:%M", time.localtime())
                status_text = f"🎧 Last.fm | {results}"
                print(f"[{time_now}] {status_text}")
                vk.status.set(text=status_text)
                last_track = results
                time.sleep(settings.INTERVAL)
            else:
                time.sleep(settings.INTERVAL)
        else:
            print("Can't get user")
            sys.exit()


if __name__ == "__main__":
    main()
