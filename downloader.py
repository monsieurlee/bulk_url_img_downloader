import csv
import os
import requests
import sys
import glob

# Function to create a folder based on the name of the CSV file if it doesn't exist
def create_csv_folder(csv_file):
    folder_name = os.path.splitext(os.path.basename(csv_file))[0]
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name

# Function to download and save an image in the folder based on the CSV file name
def download_image(url, folder_name, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_path = os.path.join(folder_name, filename)  # Set the save path
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download: {filename}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Check if a CSV file is provided as a command-line argument
if len(sys.argv) < 2:
    # If no file is dragged onto the script, find the most recent CSV file in the directory
    csv_files = glob.glob("*.csv")
    if not csv_files:
        print("No CSV files found in the directory.")
        sys.exit(1)
    csv_files.sort(key=os.path.getmtime, reverse=True)
    csv_file = csv_files[0]
else:
    csv_file = sys.argv[1]  # Get the CSV file path from the command-line argument

# Check if the CSV file exists
if not os.path.isfile(csv_file):
    print(f"CSV file '{csv_file}' not found.")
else:
    folder_name = create_csv_folder(csv_file)
    
    # Read and process the CSV file
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row if it exists

        for row in csvreader:
            if len(row) >= 2:
                url, filename = row[0], row[1]
                download_image(url, folder_name, filename)
            else:
                print("Invalid CSV format. Each row should contain URL and filename.")

print("Task completed.")
