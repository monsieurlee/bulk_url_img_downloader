# bulk_url_img_downloader
This python script allows bulk download of image from a list of URLs, and rename the files based on a list of provided file names

1. Create a CSV file in this format <url>,<filename.jpg>, lik below
https://www.site.com/image/1.jpg,alpha.jpg
https://www.site.com/image/2.jpg,bravo.jpg
https://www.site.com/image/3.jpg,charlie.jpg

1st column is the source URL, 2nd column is the filename you want it saved as.

2. Save the fils as "url.cvs". If you want to change the file name, change "url.csv" from the code.
3. Run the script.

Make sure that the'requests' library is installed, if not, run "pip install requests"
