from pytube import YouTube
import re
import os

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video(url, title,Video ,resolution='144p'):
    try:
     
        yt = YouTube(url)
        
       
        stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
        
        if stream:
          
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
            
       
            stream.download(output_path=output_path, filename=filename)
            
        else:
            print(f"No video found with {resolution} resolution for {title}")
    
    except Exception as e:
        print(f"An error occurred while downloading : {e}")

