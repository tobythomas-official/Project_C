## YouTube Playlist Information Retriever

This Python script retrieves information about playlists associated with a specific YouTube channel and determines the number of videos within each playlist.

**Requirements:**

* Python 3
* `requests` library (install using `pip install requests`)
* YouTube Data API v3 key (get one from [https://support.google.com/googleapi/answer/6158862?hl=en](https://support.google.com/googleapi/answer/6158862?hl=en))

**Instructions:**

1. Replace `YOUR_API_KEY` in the code with your actual YouTube Data API v3 key.
2. Set the `channel_id` variable to the ID of the YouTube channel you're interested in.
3. Run the script using `python youtube_playlist_info.py`.

**Output:**

The script will print the title of each playlist and the number of videos it contains.

**Code:**

```python
import requests
import json

API_KEY = "YOUR_API_KEY"  # Replace with your actual YouTube Data API v3 key
channel_id = "UCzXhzEYY6jgRRj8VNDJg4Sw"

search_url = "https://www.googleapis.com/youtube/v3/playlists"
search_params = {
    "part": "snippet",
    "channelId": channel_id,
    "type": "playlist",
    "key": API_KEY,
    "maxResults": 50,
}

search_response = requests.get(search_url, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()
    playlists = search_data.get("items", [])

    for playlist in playlists:
        playlist_title = playlist["snippet"]["title"]
        playlist_id = playlist["id"]["playlistId"]

        # Get playlist items (videos) and count
        base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet, contentDetails",
            "playlistId": playlist_id,
            "key": API_KEY,
            "maxResults": 50,
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            video_count = len(data["items"])  # Count videos directly from response

            print(f"Playlist Title: {playlist_title}")
            print(f"Number of Videos: {video_count}")
            print("-" * 40)  # Optional separator for readability

        else:
            print(f"Error getting videos for playlist '{playlist_title}': {response.status_code}, {response.text}")

else:
    print(f"Error searching playlists: {search_response.status_code}, {search_response.text}")
```

**Additional Notes:**

* The code currently retrieves a maximum of 50 videos per playlist. If a playlist has more than 50 videos, you'll need to implement pagination using the `nextPageToken` parameter in subsequent requests.
* Be mindful of YouTube Data API v3 quota limitations ([https://developers.google.com/youtube/v3/determine_quota_cost](https://developers.google.com/youtube/v3/determine_quota_cost)). Consider exponential backoff or other strategies for handling rate limits.

This README provides a clear overview of the script's functionality, requirements, instructions, and additional notes. It also includes the code itself for easy reference.
