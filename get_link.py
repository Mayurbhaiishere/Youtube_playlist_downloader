from pytube import Playlist
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

def get_links(playlist_url, output_file):
    try:
        playlist = Playlist(playlist_url)
        video_urls = [video.watch_url for video in playlist.videos]
        
        with open(output_file, 'w') as file:
            for index, url in enumerate(video_urls, start=1):
                file.write(f"{index}. {url}\n")
        
        print(f"All video links have been saved to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {output_file}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while getting links: {e}")


def save_url_to_file(Playlist_name, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(f"{Playlist_name}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving the URL to file: {e}")

def get_playlist_name(playlist_url):
    playlist = Playlist(playlist_url)
    playlist_name = playlist.title

    return playlist_name

if __name__ == "__main__":
    Playlist_url_file_path = "playlist_url.txt"
    Playlist_url = extract_url_from_file(Playlist_url_file_path)
    
    if Playlist_url:
        get_links(Playlist_url, "links.txt")

    
    Playlist_name = get_playlist_name(Playlist_url)
    save_url_to_file(Playlist_name,"playlist_name.txt")
