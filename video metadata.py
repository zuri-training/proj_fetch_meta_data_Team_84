from importlib.resources import path
import os
import subprocess


"""

Video DATA EXTRACTOR

"""
#print(f"path: {path}")
    #print(f"directories: {directories}")
    #print(f"files: {files}\n")
root_vid_directory = r"C:\Users\USER\Videos\grownish - S02E09 HD (TvShows4Mobile.Com).mp4"


    
    
    for path, directories, files in os.walk(root_vid_directory):
        for video_file in files:
            if video_file.endswith("MP4"):
            full_mp4_path = os.path.join(path, video_file)
            full_gpx_output = full_mp4_path.replace(".mp4",".GPX")
            print(f"Processing: (full_mp4_path)")
            with open(full_gpx_output_path, "w") as gpx_file:
                exiftool_command = ["C:\Program Files\exiftool\exiftool.exe", "-ee", "-m", "C:\Users\USER\Desktop\libraries\env\gpx.fmt.txt", "full_gpx_output" ]
                subprocess.run(exiftool_command, stdout=gpx_file)
            print(f"Successfully created: {full_gpx_output_path}\n")
            
            
        
        
    
    





