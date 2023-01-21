from ..plugin import Plugin
import xbmc
import json


class default_play_video(Plugin):
    name = "default video playback"
    priority = 0

    def play_video(self, item):
        item = json.loads(item)
        if item.get("link"):
            return xbmc.Player().play(item["link"])
