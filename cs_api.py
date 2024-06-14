import requests
import json
import csv

API_KEY = "AIzaSyA65ki9iwtU-iA0L00kem3IoYImi8CESgc"
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
    with open('isl_videos.csv', 'w', newline='', encoding="utf-8") as csv_file:
     csv_writer = csv.writer(csv_file)

     headers = [ 'title', 'playlist_id','video_count' ]
     csv_writer.writerow(headers)
     for playlist in playlists:
        playlist_title = playlist["snippet"]["title"]
        playlist_id = playlist["id"]
        
        base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": API_KEY,
            "maxResults": 50,
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            video_count = len(data["items"])
            csv_writer.writerow([playlist_title,playlist_id,video_count])
            # print(f"Playlist Title: {playlist_title}")
            # print(f"Number of Videos: {video_count}")
            # print("-" * 50)

        else:
            print(f"Error getting videos for playlist '{playlist_title}': {response.status_code}, {response.text}")

else:
    print(f"Error searching playlists: {search_response.status_code}, {search_response.text}")

print('fetched_isl_videocount')