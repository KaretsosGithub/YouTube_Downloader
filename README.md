YouTube Downloader
=================
A python script to download videos from *youtube* and convert them to *mp3*.

How the Script Works?
====================
This script utilizes the *pytube* library in order to find the desired video, by providing the URL and the *moviepy* library to convert the downloaded video to *mp3*, using the *libmp3lame* codec.
To save disk space, the downloaded video is deleted, after creating the corresponding *mp3* file.

How to Run the Script and Download Music?
==============================================
*Note*: The script is designed to run in a Windows system (Windows 10 for example).<br>
To specify the save location, you need to update the code with the desired path.<br>

After cloning the repo and updating the save path according to your needs:

1. Create a .txt file that contains the URLs of the videos to be downloaded and converted to mp3.<br>
   **Each line in the .txt file must contain one URL!**.
3. Run the script and provide the full path to the .txt file created in step (1).
4. Wait for the videos to be downloaded and converted to mp3.
5. A log file will also be created in the same folder as the downloaded *mp3s*.<br>
   If there is any error during the processing of the URLs, it is logged in this file, and the user is notified at the end of the script execution

Screenshots
===========

Dependencies
============
- [pytube](https://pytube.io/en/latest/)
  ``` sh
  pip install pytube
  ```
- [moviepy](https://pypi.org/project/moviepy/)
  ``` sh
  pip install moviepy
  ```
