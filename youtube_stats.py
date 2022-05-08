import json

import requests


class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_stats = None

    def get_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels/?part=statistics&id={self.channel_id}&key={self.api_key}'
        # print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data)
        # try:
        #     data = data
        # except:
        #     data = None

        self.channel_stats = data
        return data

    def dump(self):
        if self.channel_stats is None:
            return
        else:
            channel_title = "Some_name"
            channel_title = channel_title.replace(" ", "_").lower()
            file_name = channel_title + '.json'
            with open(file_name, 'w') as f:
                json.dump(self.channel_stats, f, indent=4)

