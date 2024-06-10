import json
import csv


def convert_json_to_csv(json_file_path, csv_file_path):
    """Converts a JSON file containing employee data to a CSV file.

    Args:
        json_file_path (str): Path to the JSON file.
        csv_file_path (str): Path to the output CSV file.
    """

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        video_data = data.get('video_details', [])

        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            headers = ['language', 'books', 'url', 'title', 'description', 'theme']
            csv_writer.writerow(headers)

            for video in video_data:
                url = f"https://youtu.be/{video.get('PLaIRCRKlhp7eukgRqsNDZsm4_4t5pw27f', '')}"
                title = video.get('title', '')
                description = video.get('description', '')

                csv_writer.writerow([
                    'hin',
                    url,
                    title,
                    description,
                    theme,
                      ])

        print(f"Successfully converted JSON to CSV: {csv_file_path}")

    except FileNotFoundError as e:
        print(f"Error: JSON file not found at path: {json_file_path}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in file: {json_file_path}. Please check for syntax errors or missing commas/colons.")
