from pytube import Playlist, YouTube
from tqdm import tqdm

def extract_url_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while extracting URL from file: {e}")
    return ""

def get_video_duration(video_url):
    try:
        yt = YouTube(video_url)
        return yt.length  
    except Exception as e:
        print(f"An error occurred while fetching video duration: {e}")
    return None

def save_durations_to_file(durations, filename='timestamp.txt'):
    try:
        with open(filename, 'w') as file:
            for index, (video_title, video_duration) in enumerate(durations.items(), start=1):
                file.write(f"{index}. {video_duration}\n")
                file.write("\n")
        print(f"Durations saved to {filename}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving durations to file: {e}")

def save_titles_to_file(durations, filename='titles.txt'):
    try:
        with open(filename, 'w') as file:
            for index, (video_title, video_duration) in enumerate(durations.items(), start=1):
                file.write(f"{index}. {video_title}\n")
        print(f"Titles saved to {filename}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving titles to file: {e}")

if __name__ == "__main__":
    path = "playlist_url.txt"
    url = extract_url_from_file(path)
    
    if url:
        try:
            playlist = Playlist(url)
            print(f"Fetching playlist: {playlist.title}")
            
            all_durations = {}

            for video_url in tqdm(playlist.video_urls):
                yt = YouTube(video_url)
                video_title = yt.title
                video_duration = get_video_duration(video_url)
                if video_duration is not None:
                    all_durations[video_title] = video_duration

            save_durations_to_file(all_durations)
            save_titles_to_file(all_durations)
        except Exception as e:
            print(f"An error occurred while processing the playlist: {e}")
