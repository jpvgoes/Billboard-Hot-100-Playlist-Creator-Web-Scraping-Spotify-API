# Scraping the Billboard Hot 100 and Creating a Spotify Playlist

## Project Description

This project allows the user to travel back in time to a specific year and create a Spotify playlist with the songs from the **Billboard Hot 100** for that year. It uses the **BeautifulSoup**, **Requests**, and **Spotipy** libraries to perform web scraping and automate playlist creation.

### Features

1. **User Input**:
   - The user enters a date in the format `YYYY-MM-DD` to choose the desired year.

2. **Billboard Hot 100 Web Scraping**:
   - The program accesses the Billboard website and extracts the names of the 100 most popular songs on the given date.

3. **Spotify Integration**:
   - Using the Spotify API, the program:
     - Authenticates the user.
     - Searches for the extracted songs on Spotify.
     - Creates a private Spotify playlist with the found songs.

4. **Playlist Creation**:
   - The found songs are added to the newly created playlist on Spotify.

### Program Flow

1. The user enters a valid date in the format `YYYY-MM-DD`.
2. The program validates the date and makes a request to the Billboard website to get the **Hot 100** songs.
3. The songs are searched on Spotify, and those found are added to a new private playlist.
4. At the end, the program displays a message confirming the creation of the playlist.

## Technologies Used

- **Python**: Main language of the project.
- **BeautifulSoup**: For web scraping and extracting data from the Billboard website.
- **Requests**: For making HTTP requests to the Billboard website.
- **Spotipy**: For integration with the Spotify API and automating playlist creation.

## Prerequisites

1. **Spotify Developer Account**:
   - Create an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to obtain your `CLIENT_ID` and `CLIENT_SECRET`.

2. **Install Dependencies**:
   - Run the following command to install the required libraries:
     ```bash
     pip install requests beautifulsoup4 spotipy
     ```

3. **Set Up the Environment**:
   - Replace the `CLIENT_ID` and `CLIENT_SECRET` variables in the code with the values obtained from the Spotify Developer Dashboard.

## How to Run the Project

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. Enter a date in the format `YYYY-MM-DD` when prompted.
5. Log in to Spotify when the browser opens.
6. Wait for the playlist to be created and check your Spotify profile.

## Notes

- Not all Billboard Hot 100 songs may be available on Spotify. The program will inform you which songs were skipped.
- Make sure your `CLIENT_ID` and `CLIENT_SECRET` are correct to avoid authentication errors.

## Usage Example

1. The program prompts:
   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
   ```
2. The user enters:
   ```
   2000-08-12
   ```
3. The program creates a playlist named `2000-08-12 Billboard 100` on Spotify with the available songs.

## License

This project is for educational purposes only and should not be used for commercial purposes.

---
