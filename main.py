import subprocess
import os
import time
from get_yt_vedio import download_video 

def call_script():
    try:
        
        subprocess.call(["python", "get_link.py"])
        subprocess.call(["python", "get_duration.py"])
        
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while calling the script: {e}")

def split_file_data_from_file(file_path):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(". ", 1)
                    if len(parts) > 1:
                        results.append(parts[1].strip())
                    else:
                        print(f"No '. ' found in line: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    return results

def save_url_to_file(url, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(url)
        print(f"URL saved to {file_path}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving the URL to file: {e}")


def extract_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while extracting text from file: {e}")
    return ""





def garbage_collector(file_path):
        os.remove(file_path)
        
    
        




if __name__ == "__main__":
    
    playlist_url = "https://www.youtube.com/playlist?list=PLhTjy8cBISEoYoJd-zR8EV0NqDddAjK3m"
    playlist_url_file_path = "playlist_url.txt"
    save_url_to_file(playlist_url, playlist_url_file_path)
    call_script()

    playlist_name_path = "playlist_name.txt"
    playlist_name_data = extract_text_from_file(playlist_name_path)

    timestamp_path = "timestamp.txt"
    timestamp_data = split_file_data_from_file(timestamp_path)

    links_path = "links.txt"
    links_data = split_file_data_from_file(links_path)

    titles_path = "titles.txt"
    titles_data = split_file_data_from_file(titles_path)
    
    
    for index in range(len(timestamp_data)):
        try:
            video_path = os.path.join("videos", titles_data[index])
            if os.path.isfile(video_path):
                continue
            else:
                print(f"Downloading video {index+1}...")
                download_video(links_data[index], titles_data[index],playlist_name_data)

        except ValueError:
            print(f"Invalid timestamp: {timestamp_data[index]}")
        except Exception as e:
            print(f"An error occurred: {e}")
    

    garbage_collector(playlist_name_path)
    garbage_collector(timestamp_path)
    garbage_collector(links_path)
    garbage_collector(titles_path)
    garbage_collector(playlist_url_file_path)