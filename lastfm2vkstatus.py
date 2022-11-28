import argparse
import logging
import time

import pylast
import vk_api

import settings

logger = logging.getLogger(__name__)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def get_args():
    """Parse and return provided args"""
    parser = argparse.ArgumentParser(
        description="Simple lastfm autostatus for vk.com."
    )
    parser.add_argument(
        "--verbose",
        action="count",
        default=False,
        help="Outputs verbose status messages",
    )

    return parser.parse_args()


def init_lastfm(api_key, api_secret, username, password):
    """Init Last.fm instance"""
    logger.debug("init lastfm instance")
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
        username=username,
        password_hash=pylast.md5(password),
    )
    lastfm = network.get_user(username)
    return lastfm


def init_vk(vk_user_token):
    """Init VK instance"""
    logger.debug("init vk instance")
    vk_session = vk_api.VkApi(token=vk_user_token)
    vk = vk_session.get_api()
    return vk


def handle_now_playing(lastfm, vk):
    """Infinite check of lastfm now playing to update vk.com status"""
    logger.debug("start status update handler")
    last_track = ""
    while True:
        logger.debug("get lastfm now playing")
        now_playing = lastfm.get_now_playing()
        if now_playing:
            if now_playing != last_track:
                status_text = f"🎧 Last.fm | {now_playing}"
                logger.info(status_text)
                vk.status.set(text=status_text)
                last_track = now_playing
        else:
            if last_track:
                logger.debug(f"status cleared ({last_track} -> '')")
                last_track = ""
                vk.status.set(text=last_track)
        time.sleep(settings.INTERVAL)


def main():
    args = get_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.info("Verbose output.")

    lastfm = init_lastfm(
        api_key=settings.API_KEY,
        api_secret=settings.API_SECRET,
        username=settings.USERNAME,
        password=settings.PASSWORD,
    )
    vk = init_vk(vk_user_token=settings.VK_USER_TOKEN)
    handle_now_playing(lastfm=lastfm, vk=vk)


if __name__ == "__main__":
    main()
