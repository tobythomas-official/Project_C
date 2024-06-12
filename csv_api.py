import requests
import csv


API_KEY = "AIzaSyA65ki9iwtU-iA0L00kem3IoYImi8CESgc"
playlist_id = "PLdE_o99zEY27qphIt6afYSZn0zM7nP1qF"
base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
params = {
  "part": "snippet, contentDetails",
  "playlistId": playlist_id,
  "key": API_KEY,
  "maxResults": 50,
  }

response = requests.get(base_url, params=params)
print(response)
if response.status_code == 200:
   data = response.json()
   print(data)
   with open('bible_videos.csv', 'w', newline='', encoding="utf-8") as csv_file:
     csv_writer = csv.writer(csv_file)
     
     headers = ['language', 'url', 'title', 'description', 'theme']
     csv_writer.writerow(headers)
     
     for item in data["items"]:
        video_id= item["snippet"]["resourceId"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        url = f"https://youtu.be/{video_id}"
        csv_writer.writerow([
           'hin',
           url,
           title,
           description,
           'Old Testament',
           ])
        print(f"Successfully saved videos to bible_videos.csv")
else:
    print("Error:", response.status_code, response.text)