This python script allows bulk download of image from a list of URLs, and rename the files based on a list of provided file names

Make sure that the 'requests' library is installed, if not, run "pip install requests"

1. Create a CSV file in this format ,<filename.jpg>, like below

url, filename
https://www.site.com/image/1.jpg,alpha.jpg

https://www.site.com/image/2.jpg,bravo.jpg

https://www.site.com/image/3.jpg,charlie.jpg

1st column is the source URL, 2nd column is the filename you want it saved as.

2. Save the fils as CSV.

3. Drag the CSV file on the script, or run it. If you just run it, it'll use the most recent CSV file in the dir

Script will create a new folder on the root level with the name of the CSV file and save all images in there

Currently only tested with .jpg
