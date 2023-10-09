# Spotify Playlist Scraper

This Python script allows you to scrape data from Spotify's website, including playlist and audiobook information, along with their image URLs. It leverages Selenium for web automation and BeautifulSoup for HTML parsing.

## Prerequisites

- Python 3.x
- Selenium (Python package)
- BeautifulSoup (Python package)
- Chrome WebDriver

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages using pip:

        pip install selenium beautifulsoup4


3. Download and install the Chrome WebDriver. You can find it here: [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)

## Usage

1. Open the `scraper.py` file in your code editor.

2. Configure the script:

- Ensure you have set up the correct path to the Chrome WebDriver.

- Modify the URL (`driver.get("https://open.spotify.com/")`) to the Spotify page you want to scrape data from.

3. Run the script:

        python scraper.py

4. The script will scrape data from the specified Spotify page, including playlist and audiobook information along with image URLs.

5. The scraped data will be saved in a JSON file named `spotify_playlists_with_images.json`.

## Utilizing the Scraped Data

You can utilize the scraped data in various ways, such as:

- **Data Analysis:** Load the JSON data into your Python code and perform data analysis or visualization to gain insights.

- **Web Development:** If you're a web developer, you can use the scraped data to build web applications, dashboards, or websites that display Spotify playlist information.

- **Data Integration:** Integrate the data into other applications or services for further processing or use.

## preview
This how this data looks with some css
<img width="1290" alt="Screenshot 2023-10-09 at 1 16 53 PM" src="https://github.com/LakGar/web-scrapper/assets/90293130/e8d50972-d289-468f-817e-b3ed6945c94d">
<img width="1290" alt="Screenshot 2023-10-09 at 1 16 58 PM" src="https://github.com/LakGar/web-scrapper/assets/90293130/5aa0071a-b88c-472c-a583-851362c2c6a0">


## Contributing

Feel free to contribute to this project by improving the code or adding new features. Pull requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created for educational purposes and to demonstrate web scraping using Python.


