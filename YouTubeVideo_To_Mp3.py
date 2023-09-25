"""
------------------------------------------------
------------------------------------------------
--------------- A Python Script ----------------
------------ to Download Songs from ------------
------------------ YouTube ---------------------
------------------------------------------------
--- 1) Create a text file with the video URLs --
------- Each line must contain 1 URL! ----------
--- 2) Execute the script and provide the ------
----------- path to the text file --------------
- The script will find and download the videos -
-------- and convert them to mp3 format --------
------------------------------------------------
------------------------------------------------
------------------------------------------------

"""

# -----------------------------------------------
# -----------------------------------------------

import os
import re
from pytube import YouTube
from moviepy.editor import VideoFileClip

# -----------------------------------------------
# -----------------------------------------------

def sanitize_file_name(file_name):
    # Replace invalid characters with underscores and remove any consecutive underscores
    sanitized_name = re.sub(r'[<>:"/\\|?*@]', '_', file_name)
    sanitized_name = re.sub(r'_+', '_', sanitized_name)
    
    # Remove leading and trailing underscores
    sanitized_name = sanitized_name.strip('_')
    
    return sanitized_name

# -----------------------------------------------
# -----------------------------------------------

def download_and_convert(video_url, output_folder):
    try:
        # Initialize YouTube object
        youtube = YouTube(video_url)
        
        # Sanitize the video title before saving the file
        video_title = sanitize_file_name(youtube.title)
        
        # Get the highest resolution stream available
        video_stream = youtube.streams.filter(file_extension='mp4').get_highest_resolution()

        # Specify the download location for the video
        video_path = os.path.join(output_folder, f"{video_title}.mp4")
        video_stream.download(output_path=output_folder, filename=f"{video_title}.mp4")

        print(f"----> Video '{video_title}' downloaded as MP4 successfully.")
        print()

        # Convert the downloaded video to MP3
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        mp3_path = os.path.join(output_folder, f"{video_title}.mp3")
        audio_clip.write_audiofile(mp3_path, codec="libmp3lame", bitrate="128k")

        print(f"----> Video '{video_title}' converted to MP3 with 128 kbps successfully.")
        print()
        
        # Close the video clip
        video_clip.close()
        
        # Remove the downloaded video file
        os.remove(video_path)
        print(f"----> Video '{video_title}.mp4' removed.")
        print("------" * 15)
        print()
        
    except Exception as e:
        error_message = f"Error occurred on line {line_number}: {video_url.strip()}\n{str(e)}\n\n"
        print(f"----> {error_message}")
    
        # Write the error message to the log file
        log_file.write(error_message)

# -----------------------------------------------
# -----------------------------------------------

def get_text_file_path():
    while True:
        # User must provide a valid path
        print("Please enter the full path to the text file containing video URLs and press Enter:")
        file_path = input()

        if os.path.isfile(file_path):
            return file_path
        else:
            print()
            print("------" * 15)
            print("+++++" * 15)
            print("Invalid file path. Please provide a valid file path.")
            print("+++++" * 15)
            print("------" * 15)
            print()
            
# -----------------------------------------------
# -----------------------------------------------

def check_for_errors(log_file_path):
    # Notify the user if script has logged any errors in the log file
    with open(log_file_path, "r") as log_file:
        log_contents = log_file.read()
        if "Error occurred" in log_contents:
            print("------" * 25)
            print(f"Error(s) detected in the log file. Please check log file at {log_file_path}")
            print("------" * 25)
            
# -----------------------------------------------
# -----------------------------------------------

def print_welcome_message():
    welcome_message = """
    -----------------------------------------------
    -----------------------------------------------
    ---------- YouTube Video Downloader -----------
    -----------------------------------------------
    -----------------------------------------------
    
                     Welcome!
    
    This script allows you to download YouTube videos
    and convert them to mp3 format. Simply provide a
    text file containing the URLs of the videos you
    want to download.
    
    -----------------------------------------------
    -----------------------------------------------
    """
    print(welcome_message)

# -----------------------------------------------
# -----------------------------------------------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# -----------------------------------------------
# -----------------------------------------------

# Print welcome message
print_welcome_message()
print("------" * 15)

# Create the 'MP3s' folder if is doesn't exist
# Update the path, according to your needs.
mp3s_folder = r'D:\Downloads\MP3s'
if not os.path.exists(mp3s_folder):
        os.makedirs(mp3s_folder)
        
# Create a log file in the same folder as downloaded MP3s
# It will be used to record any errors
log_file_path = os.path.join(mp3s_folder, "error_log.txt")

# Always create a new log file, overwriting any existing one
log_file = open(log_file_path, "w")
    
# Get the path to the text file containing video URLs from the user manually
file_path = get_text_file_path()
with open(file_path, 'r') as file:
    print(f"----> File found and opened: '{file_path}'")
    print("------" * 15)
    video_urls = file.readlines()
    print()
    
#Proccess the txt file containing the URLs
for line_number, url in enumerate(video_urls, start=1):
    print(f"Processing line {line_number}: {url.strip()}")
    download_and_convert(url.strip(), output_folder=mp3s_folder)
    
# Close the log file, in order ensure that any buffered data is flushed to the file
log_file.close()

# Check for errors in the log file
check_for_errors(log_file_path)

print("------" * 15)
print("\n----> Program done!")
# -----------------------------------------------
# -----------------------------------------------