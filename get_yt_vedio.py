import yt_dlp
import re
import os

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(url, title, Video, resolution='900p'):
    try:
        sanitized_title = sanitize_filename(title)
        filename = f"{sanitized_title}.mp4"
        
        new_dir = Video
        output_path = os.path.join(os.getcwd(), new_dir)
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        full_path = os.path.join(output_path, filename)

        if os.path.exists(full_path):
            try:
                os.remove(full_path)
            except PermissionError:
                print(f"Permission denied: unable to remove existing file {full_path}")
                return
        
        ydl_opts = {
            'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',  
            'outtmpl': full_path, 
            'noplaylist': True,   
            'quiet': True,       
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {title} at {resolution} resolution")

    except Exception as e:
        print(f"An error occurred while downloading: {e}")

