import sqlite3 
conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def main():
    while true:
        print("\n Youtube manager app with DB")
        print("\n 1.List videos.")
        print("\n 2.Add videos.")
        print("\n 3.Update videos.")
        print("\n 4.Delete video.")
        print("\n 5.Exit app.")
if __name__ == "main":
    main()