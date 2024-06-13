import requests
import csv


API_KEY = "AIzaSyA65ki9iwtU-iA0L00kem3IoYImi8CESgc"
channel_id = "UCzXhzEYY6jgRRj8VNDJg4Sw"

search_url = "https://www.googleapis.com/youtube/v3/search"
search_params = {
    "part": "snippet",
    "channelId": channel_id,
    "type": "playlist",
    "maxResults": 10,
    "key": API_KEY,
}

search_response = requests.get(search_url, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()
    playlists = search_data.get("items", [])

    if playlists:
        chosen_playlist_id = playlists[0]["id"]["playlistId"]

        base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet, contentDetails",
            "playlistId": chosen_playlist_id,
            "key": API_KEY,
            "maxResults": 50,
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error getting videos: {response.status_code}, {response.text}")
    else:
        print(f"No playlists found for channel {channel_id}")
else:
    print(f"Error searching playlists: {search_response.status_code}, {search_response.text}")
