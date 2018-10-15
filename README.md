# lastfm2vkstatus

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/95b4fb07dce64f1185bfdac8d97f30ab)](https://app.codacy.com/app/DiSonDS/lastfm2vkstatus?utm_source=github.com&utm_medium=referral&utm_content=DiSonDS/lastfm2vkstatus&utm_campaign=Badge_Grade_Dashboard)

Use currently playing track as status in VK.com

## Requirements
-   pylast
-   vk_api

## Setup

### Last.fm
1.  Obtain your api_key, api_secret from <https://www.last.fm/api/account/create>
2.  Complete the **settings.py** with last.fm api_key, api_secret, username, password

### VK.com
1.  Obtain your access token: <https://vk.cc/8Abj47>
2.  Complete the **settings.py** with token

## Usage

```console
python3 lastfm2vkstatus.py
```
![Screenshot](screenshot.png)
