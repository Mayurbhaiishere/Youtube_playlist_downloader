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

def save_titles_to_file(titles, filename='titles.txt'):
    try:
        with open(filename, 'w') as file:
            for index, video_title in enumerate(titles, start=1):
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
            
            all_titles = []

            for video_url in tqdm(playlist.video_urls):
                yt = YouTube(video_url)
                video_title = yt.title
                all_titles.append(video_title)

            save_titles_to_file(all_titles)
        except Exception as e:
            print(f"An error occurred while processing the playlist: {e}")
