#!/usr/bin/env python3

import json
from podgen import Podcast, Episode, Media
from datetime import datetime
import pytz

MEDIA_BASE_URL="https://boggle.org/thebugle"

def main():
    with open('thebugle.json') as f:
        episodes = json.load(f)

    p = Podcast(
        name="TimesOnLine Bugle Archive",
        description="Old Bugle episodes, podcast feed",
        website="http://example.org/animals-alphabetically",
        explicit=False,
    )
    
    for episode in episodes:
        ep = p.add_episode(Episode(
            title=f"{episode['id']}: {episode['title']}"
        ))
        ep.media = Media.create_from_server_response(
            f"{MEDIA_BASE_URL}/{episode['file']}"
        )

        ep.media.fetch_duration()

        date = episode['date'].split('-')
        ep.publication_date = datetime(int(date[0]), int(date[1]), int(date[2]), 0, 0, 0, tzinfo=pytz.utc)

    print(p.rss_str())

if __name__ == "__main__":
    main()
