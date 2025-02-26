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

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    cursor.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    cursor.commit()

def delete_video():
    pass

def main():
    while true:
        print("\n Youtube manager app with DB")
        print("\n 1.List videos.")
        print("\n 2.Add videos.")
        print("\n 3.Update videos.")
        print("\n 4.Delete video.")
        print("\n 5.Exit app.")
        choice = input("\n Enter your choice:")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("\n Enter the video name:")
            time = input("\n Enter the video time:")
            add_video(name,time)
        elif choice == '3':
            video_id = input("\n Enter the video ID to update:")
            name = input("\n Enter the video name:")
            time = input("\n Enter video time:")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("\n Enter the video ID to delete:")
            delete_video(video_id)
        elif choice == '5':
            break 
        else :
            print("\nInvalid choice.")

        conn.close()
if __name__ == "main":
    main()