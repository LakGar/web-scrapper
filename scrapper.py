import time
from selenium import webdriver
from bs4 import BeautifulSoup
import json

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed.
driver.get("https://open.spotify.com/")
# Wait for the page to load (you might need to adjust the sleep time)
time.sleep(1)
# Get the page source after dynamic content has loaded
page_source = driver.page_source
# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all sections with the specified class
sections = soup.find_all('section', class_="QyANtc_r7ff_tqrf5Bvc Shelf")

# Create a list to store playlist and audiobook data along with their image URLs
playlist_data_with_images = []

# Iterate through each section and find the h2 element
for section in sections:
    list_titles = section.find_all("a", class_="MfVrtIzQJ7iZXfRWg6eM")
    for list_title in list_titles:
        playlist_data = {}
        playlist_title = list_title.text.strip()
        playlist_url = list_title['href']  # Extract the href attribute

        complete_playlist_url = f"https://open.spotify.com{playlist_url}"
        driver.get(complete_playlist_url)
        time.sleep(1)
        page_source = driver.page_source
        playlist_soup = BeautifulSoup(page_source, 'html.parser')

        # Now, you can send a request to scrape the playlist or audiobook page
        image_urls = playlist_soup.find_all('img', class_="mMx2LUixlnN_Fu45JpFB SKJSok3LfyedjZjujmFt Yn2Ei5QZn19gria6LjZj")
        endpoints = playlist_soup.find_all('a', class_="Nqa6Cw3RkDMV8QnYreTr")
        playlist_type = playlist_soup.find('h2', class_='Type__TypeElement-sc-goli3j-0 kqHgh MfVrtIzQJ7iZXfRWg6eM')
        playlist_data['type'] = playlist_type.text
        playlist_data['playlists'] = []

        for endpoint, image_url in zip(endpoints, image_urls):
            playlist_info = {}
            endpoint_url = endpoint['href']
            new_url = f"https://open.spotify.com{endpoint_url}"

            driver.get(new_url)
            time.sleep(1)
            page_source = driver.page_source
            main_page = BeautifulSoup(page_source, 'html.parser')

            titles = main_page.find('h1', class_="Type__TypeElement-sc-goli3j-0 dYGhLW")
            playlist_info['title'] = titles.text

            
            if image_url:
                playlist_info['image_url'] = image_url.get('src')

            description = main_page.find('div', class_='xgmjVLxjqfcXK5BV_XyN fUYMR7LuRXv0KJWFvRZA')
            if description:
                playlist_info['description'] = description.text
            else:
                author = main_page.find('span', class_="Type__TypeElement-sc-goli3j-0 bnCeva")
                playlist_info['author'] = author.text

            # Check if likes element exists
            likes = main_page.find('span', class_='Type__TypeElement-sc-goli3j-0 ieTwfQ RANLXG3qKB61Bh33I0r2')
            if likes:
                playlist_info['likes'] = likes.text
            else:
                price = main_page.find('span', class_='Type__TypeElement-sc-goli3j-0 kqHgh')
                playlist_info['price'] = price.text

            duration = main_page.find('span', class_='poz9gZKE7xqFwgk231J4')
            if duration:
                playlist_info['duration'] = duration.text
            else:
                book_duration = main_page.find('span', class_='UyzJidwrGk3awngSGIwv')
                playlist_info['book_duration'] = book_duration.text

            num_of_songs = main_page.find('span', class_='Type__TypeElement-sc-goli3j-0 ieTwfQ RANLXG3qKB61Bh33I0r2')
            if num_of_songs:
                playlist_info['number_of_songs'] = num_of_songs.text
            else:
                published_date = main_page.find('span', class_='Type__TypeElement-sc-goli3j-0 ieTwfQ QOp2aYTYmZHZ6DFFHuYE')
                playlist_info['published_on'] = published_date.text

            song_cards = main_page.find_all('div', class_="h4HgbO_Uu1JYg5UGANeQ wTUruPetkKdWAR1dd6w4")
            playlist_info['songs'] = []

            for song_card in song_cards:
                song_info = {}
                song_img_url = song_card.find('img').get('src')
                song_name = song_card.find('div', class_='Type__TypeElement-sc-goli3j-0 fZDcWX t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')
                song_artist = song_card.find('span', class_='Type__TypeElement-sc-goli3j-0 bDHxRN rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line')
                song_album = song_card.find('a', class_='standalone-ellipsis-one-line')
                song_date_added = song_card.find('span', class_='Type__TypeElement-sc-goli3j-0 bDHxRN')
                song_duration = song_card.find('div', class_='Type__TypeElement-sc-goli3j-0 bDHxRN Btg2qHSuepFGBG6X0yEN')
                song_info['song_img_url'] = song_img_url
                song_info['song_name'] = song_name.text
                song_info['song_artist'] = song_artist.text
                song_info['song_album'] = song_album.text
                song_info['song_date_added'] = song_date_added.text
                song_info['song_duration'] = song_duration.text
                playlist_info['songs'].append(song_info)

            playlist_data['playlists'].append(playlist_info)
        playlist_data_with_images.append(playlist_data)

# Close the Selenium webdriver after processing
driver.quit()

# Convert the data to JSON format and save it to a file
with open('spotify_playlists_with_images.json', 'w', encoding='utf-8') as json_file:
    json.dump(playlist_data_with_images, json_file, ensure_ascii=False, indent=4)

print("Data saved to spotify_playlists_with_images.json")
