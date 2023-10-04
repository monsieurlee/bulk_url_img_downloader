import csv
import os
import requests

# Function to download and save an image
def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {filename}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Input CSV file name
csv_file = 'url.csv'  # Replace with your CSV file name

# Check if the CSV file exists
if not os.path.isfile(csv_file):
    print(f"CSV file '{csv_file}' not found.")
else:
    # Read and process the CSV file
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row if it exists

        for row in csvreader:
            if len(row) >= 2:
                url, filename = row[0], row[1]
                download_image(url, filename)
            else:
                print("Invalid CSV format. Each row should contain URL and filename.")

print("Task completed.")
