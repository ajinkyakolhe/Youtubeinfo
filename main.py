from youtube_stats import YTstats
API_KEY = "<Enter API Key>"
channel_id = "UCytWPg15z23p1QGMp_vCUVw"
ytstats = YTstats(API_KEY, channel_id)
ytstats.get_stats()
ytstats.dump()
