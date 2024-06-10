import requests

API_KEY = "AIzaSyA65ki9iwtU-iA0L00kem3IoYImi8CESgc"

playlist_id = "PLaIRCRKlhp7eukgRqsNDZsm4_4t5pw27f"

base_url = "https://www.googleapis.com/youtube/v3/playlistItems"

params = {
    "part": "snippet,contentDetails",  
    "playlistId": playlist_id,
    "key": API_KEY,
    "maxResults": 50,
}

response = requests.get(base_url, params=params)


if response.status_code == 200:
    data = response.json()
   
    for item in data["items"]:
        video_id = item["snippet"]["resourceId"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]  

        print(f"Video ID: {video_id}, Title: {title}, Description: {description}")
else:
    print("Error:", response.status_code, response.text)