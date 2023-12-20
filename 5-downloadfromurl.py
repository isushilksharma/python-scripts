#Python script to download a file from a given URL.

import urllib.request

def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)

# Example usage:
file_url = "https://example.com/file.txt"
destination_path = "/path/to/save/file.txt"
download_file(file_url, destination_path)
