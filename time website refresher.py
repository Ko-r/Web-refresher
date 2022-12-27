import time
import webbrowser

# Set the URL of the webpage you want to reload
url = "https://app.veve.me/market/browse/comics/90cd8e7b-5195-4f5b-a5be-bc41d9e338fa"

# Set the number of seconds you want to wait between reloads
reload_time = 10

while True:
    # Open the webpage in the default web browser
    webbrowser.open(url)
    
    # Wait for the specified number of seconds
    time.sleep(reload_time)
