# YouTube Video Manager App with SQLite Database

## Description
This is a simple command-line application to manage a list of YouTube videos using an SQLite database. Users can add, update, delete, and list videos along with their durations.

## Features
- List all stored YouTube videos.
- Add new videos with name and duration.
- Update video details.
- Delete a video from the database.
- Uses SQLite for persistent storage.

## Prerequisites
Ensure you have Python installed on your system.

## Installation
1. Clone the repository or download the `youtube_manager.py` file.
2. Ensure you have `sqlite3` (included with Python) available.
3. Run the script using:
   ```sh
   python youtube_manager.py
   ```

## Usage
1. When the script runs, it displays a menu:
   - `1`: List all stored videos.
   - `2`: Add a new video.
   - `3`: Update an existing video.
   - `4`: Delete a video.
   - `5`: Exit the application.
2. Follow the on-screen prompts to manage the videos.

## Database Schema
The application creates an SQLite database (`youtube_videos.db`) with a table `videos` that has the following columns:
- `id` (INTEGER, Primary Key, Auto-incremented)
- `name` (TEXT, Video Name)
- `time` (TEXT, Video Duration)


## Contributing
Feel free to fork and improve the project by adding new features, optimizing database queries, or enhancing the UI.



